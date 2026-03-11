# FastAPI utilities for routing, file upload, form input and error handling
from fastapi import APIRouter, UploadFile, File, Form, HTTPException

# Import service layer functions responsible for AI processing
from services.extractor import extract_requirements
from services.risk_analyzer import analyze_risks
from services.task_planner import plan_tasks
from services.parser import parse_pdf_upload


# Create router instance for grouping related API endpoints
router = APIRouter()


# API endpoint: Analyze requirement text input
@router.post("/api/analyze-text")
async def analyze_text_api(text: str = Form(...)):
    try:
        # Step 1: Extract structured requirements from raw text
        requirements = extract_requirements(text)

        # Step 2: Identify technical and business risks
        risks = analyze_risks(text)

        # Step 3: Generate task plan (Epics → Stories → Tasks)
        tasks = plan_tasks(requirements, risks)

        # Return structured analysis result
        return {
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        # Return HTTP 500 error if processing fails
        raise HTTPException(status_code=500, detail=str(e))


# API endpoint: Analyze uploaded PDF requirement document
@router.post("/api/analyze-pdf")
async def analyze_pdf_api(file: UploadFile = File(...)):
    try:
        # Convert uploaded PDF into raw text
        pdf_text = await parse_pdf_upload(file)

        # Run AI pipeline on extracted text
        requirements = extract_requirements(pdf_text)
        risks = analyze_risks(pdf_text)
        tasks = plan_tasks(requirements, risks)

        return {
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UI endpoint: Analyze text input from dashboard interface
@router.post("/ui/analyze-text")
async def analyze_text_ui(text: str = Form(...)):
    try:
        requirements = extract_requirements(text)
        risks = analyze_risks(text)
        tasks = plan_tasks(requirements, risks)

        return {
            "status": "success",
            "source": "ui",
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UI endpoint: Analyze PDF uploaded through dashboard
@router.post("/ui/analyze-pdf")
async def analyze_pdf_ui(file: UploadFile = File(...)):
    try:
        pdf_text = await parse_pdf_upload(file)

        requirements = extract_requirements(pdf_text)
        risks = analyze_risks(pdf_text)
        tasks = plan_tasks(requirements, risks)

        return {
            "status": "success",
            "source": "ui",
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))