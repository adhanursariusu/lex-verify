from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
import sys

app = FastAPI(
    title="LexVerify API",
    description="Academic Smart Contract Compliance & Vulnerability Analyzer Backend",
    version="1.0.0"
)

class AnalysisRequest(BaseModel):
    contract_address: str
    network: str = "mainnet"

@app.get("/")
def read_root():
    return {
        "status": "online",
        "project": "LexVerify",
        "institution": "Universitas Sumatera Utara",
        "purpose": "Academic Research & Thesis Development"
    }

@app.post("/analyze/address")
async def analyze_address(payload: AnalysisRequest):
    # Mocking analysis pipeline for deployment verification
    return {
        "address": payload.contract_address,
        "network": payload.network,
        "status": "completed",
        "security_score": 92,
        "compliance_status": {
            "civil_code_1320_compliant": True,
            "regulatory_flagged_functions": []
        },
        "findings": [
            {
                "id": "LV-001",
                "severity": "Low",
                "title": "Solidity Compiler Version",
                "description": "The contract uses a floating pragma."
            }
        ]
    }

@app.post("/analyze/file")
async def analyze_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".sol"):
        raise HTTPException(status_code=400, detail="Only .sol files are supported.")
    
    content = await file.read()
    # Dummy processing of file content
    return {
        "filename": file.filename,
        "lines_processed": len(content.splitlines()),
        "status": "ready_for_ast_parsing"
    }
