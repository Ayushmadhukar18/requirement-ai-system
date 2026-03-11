from services.extractor import extract_requirements
from services.risk_analyzer import analyze_risks
from services.task_planner import plan_tasks


def run_analysis_pipeline(text: str):
    """
    Runs the full AI analysis pipeline:
    1. Requirement extraction
    2. Risk analysis
    3. Task planning
    """

    # Stage 1: Extract structured requirements
    requirements = extract_requirements(text)

    # Stage 2: Identify risks and ambiguities
    risks = analyze_risks(text)

    # Stage 3: Generate engineering task plan
    tasks = plan_tasks(requirements, risks)

    return {
        "requirements": requirements,
        "risks": risks,
        "task_plan": tasks
    }