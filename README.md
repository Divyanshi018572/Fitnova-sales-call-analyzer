# FitNova Sales-Call Intelligence

This repository contains the prototype for the FitNova Sales-Call Intelligence system. The system automatically ingests, transcribes, diarises, scores, and flags sales calls for FitNova wellness and fitness coaching programs.

## System Architecture Overview

The system runs as three dockerized services:
1. **Database (`db`)**: PostgreSQL 15 database storing organizations, teams, advisors, calls, transcripts, scores, tags, and contest records.
2. **API Backend (`api`)**: FastAPI service running the orchestration pipeline (Ingestion -> Transcription -> Analysis -> Storage) and serving rollup metrics.
3. **Dashboard (`dashboard`)**: Streamlit application providing custom views for the Sales Director, Team Leaders, and Advisors.

---

## Local Setup & Run

To build and run all services locally, run:

```bash
docker-compose up --build
```

- **FastAPI API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **FastAPI Base URL**: [http://localhost:8000](http://localhost:8000)
- **Streamlit Dashboard**: [http://localhost:8501](http://localhost:8501)

---

## Deployed Services

- **API Web Service**: *(To be populated upon Render deploy)*
- **Streamlit Dashboard**: *(To be populated upon Render deploy)*

---

## Real vs. Mocked Systems

| Component | Status | Description |
|---|---|---|
| Ingestion Source | Mocked | Ingests calls from a local directory (`data/mock_calls/`) rather than live telephony webhooks. |
| Transcription / Diarisation | Real | Runs locally using `faster-whisper` and split-channel diarisation. |
| Call Scoring / Tagging | Real | Integrates with Gemini 2.5 Flash API with automated fallback to Groq Llama 3.3. |
| Database Storage | Real | Persists all call records, transcripts, scores, and tags to a PostgreSQL database. |
| Organization Rollups | Real | Computes live averages and trends per team and advisor on database records. |
| Feedback Loop / Contests | Real | Allows advisors to contest tags and team leaders to resolve contests via DB updates. |
