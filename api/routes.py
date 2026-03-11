# FastAPI utilities for routing, file upload, form input and error handling
from fastapi import APIRouter, UploadFile, File, Form, HTTPException

# Import pipeline orchestrator
from services.pipeline import run_analysis_pipeline

# Import PDF parser
from services.parser import parse_pdf_upload


# Create router instance for grouping related API endpoints
router = APIRouter()


# API endpoint: Analyze requirement text input
@router.post("/api/analyze-text")
async def analyze_text_api(text: str = Form(...)):
    try:
        # Run full AI analysis pipeline
        result = run_analysis_pipeline(text)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# API endpoint: Analyze uploaded PDF requirement document
@router.post("/api/analyze-pdf")
async def analyze_pdf_api(file: UploadFile = File(...)):
    try:
        # Convert uploaded PDF into raw text
        pdf_text = await parse_pdf_upload(file)

        # Run AI pipeline
        result = run_analysis_pipeline(pdf_text)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UI endpoint: Analyze text input from dashboard interface
@router.post("/ui/analyze-text")
async def analyze_text_ui(text: str = Form(...)):
    try:
        result = run_analysis_pipeline(text)

        return {
            "status": "success",
            "source": "ui",
            **result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UI endpoint: Analyze PDF uploaded through dashboard
@router.post("/ui/analyze-pdf")
async def analyze_pdf_ui(file: UploadFile = File(...)):
    try:
        pdf_text = await parse_pdf_upload(file)

        result = run_analysis_pipeline(pdf_text)

        return {
            "status": "success",
            "source": "ui",
            **result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))