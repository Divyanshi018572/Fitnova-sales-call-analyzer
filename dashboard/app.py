"""
Streamlit dashboard entrypoint for FitNova Sales-Call Intelligence.

Why this approach:
Streamlit provides a fast, pure-Python workflow to develop dashboards. It supports
real-time reactive updates and provides a polished interface without requiring a 
separate Javascript framework build step, staying within our prototype development budget.
"""

import streamlit as st
import os

st.set_page_config(
    page_title="FitNova Call Intelligence",
    page_icon="💪",
    layout="wide"
)

st.title("💪 FitNova Sales-Call Intelligence")
st.markdown("---")
st.subheader("Welcome to the FitNova Sales-Call Analytics Dashboard!")
st.write("This dashboard displays call metrics, advisor performance, compliance tags, and team trends.")
st.info(f"API Target Host: {os.getenv('API_URL', 'http://localhost:8000')}")
