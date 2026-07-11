"""
PII Redactor for FitNova Sales-Call Intelligence.

Why this approach:
We use a high-performance, regex-based PII redactor that runs 100% locally on CPU. 
This avoids pulling in heavy NLP packages (like Microsoft Presidio or Spacy) which would
bloat our Docker image and significantly slow down transcription on CPU.
It targets emails, phone numbers, credit cards, Indian Aadhaar IDs, and PAN cards.
"""

import re

# Regex patterns for various PII types
EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# Matches international and Indian phone formats (e.g. +91 98765 43210, 9876543210, etc.)
PHONE_PATTERN = re.compile(
    r'\+?(?:91|1)?[ -]?(?:\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}|\d{5}[ -]?\d{5}|\d{10})\b'
)

# Matches standard credit cards (13 to 16 digits)
CARD_PATTERN = re.compile(r'\b(?:\d[ -]*?){13,16}\b')

# Matches Indian Aadhaar Cards (e.g. 1234 5678 9012 or 12-digit continuous)
AADHAAR_PATTERN = re.compile(r'\b\d{4}\s\d{4}\s\d{4}\b|\b\d{12}\b')

# Matches Indian PAN Cards (e.g. ABCDE1234F)
PAN_PATTERN = re.compile(r'\b[A-Z]{5}\d{4}[A-Z]\b', re.IGNORECASE)

def redact_text(text: str) -> str:
    """
    Scans the input text and redacts sensitive PII fields.
    
    Args:
        text (str): Raw transcribed text segment.
        
    Returns:
        str: Redacted text.
    """
    if not text:
        return ""
        
    # Order matters: check cards and IDs before generic phone numbers to avoid overlap collision
    text = EMAIL_PATTERN.sub("[EMAIL_REDACTED]", text)
    text = CARD_PATTERN.sub("[CREDIT_CARD_REDACTED]", text)
    text = AADHAAR_PATTERN.sub("[AADHAAR_REDACTED]", text)
    text = PAN_PATTERN.sub("[PAN_REDACTED]", text)
    text = PHONE_PATTERN.sub("[PHONE_REDACTED]", text)
    
    return text
