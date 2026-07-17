# LexVerify: Academic Smart Contract Compliance & Vulnerability Analyzer

An open-source academic research prototype designed to bridge the gap between smart contract execution states and legal compliance. This project is developed as part of an undergraduate thesis at Universitas Sumatera Utara (USU).

## Overview

LexVerify parses Solidity Abstract Syntax Trees (ASTs) to identify security vulnerabilities (using static analysis tools like Slither) and maps contract parameters against regulatory frameworks (such as Bappebti regulations on tokenized assets and Indonesian Civil Code contract validity standards).

## Architecture

- **Backend:** Python (FastAPI), PySolc, Slither
- **Database:** PostgreSQL (for caching parsed contract metadata)
- **Frontend:** React / Tailwind CSS
- **Deployment Target:** DigitalOcean Droplet / App Platform

## VPS Resource Usage Profile

To reassure hosting providers and maintain platform compliance:
- **No outbound port scanning:** The application only performs inbound HTTP/HTTPS requests to public RPC nodes (e.g., Infura, Alchemy) or processes uploaded Solidity files locally.
- **No intensive computation/mining:** The workload is strictly limited to static AST analysis and database indexing.
- **Resource limiters:** Docker-contained processes with strict CPU (capped at 1.5 cores) and RAM (capped at 2GB) limits.

## Project Structure

```text
├── api/
│   ├── main.py            # FastAPI Application Entry
│   ├── analyzer.py        # AST and Slither parsing wrapper
│   └── compliance.py      # Regulatory rule-mapping engine
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup & Local Run

1. Clone the repository:
   ```bash
      git clone https://github.com/yourusername/lex-verify.git
   cd lex-verify
   ```

2. Run via Docker Compose:
   ```bash
   docker-compose up --build
   ```
