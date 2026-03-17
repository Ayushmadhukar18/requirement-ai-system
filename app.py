from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
import os

load_dotenv()

from api.routes import router
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env in the project root
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)
import os
# Debug check (temporary)

# Create FastAPI application instance
=======
>>>>>>> upstream/main
app = FastAPI(
    title="Requirement Intelligence Agent",
    version="1.0"
)

#
# -------- STATIC + TEMPLATES --------
#

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


#
# -------- UI HOME PAGE --------
#

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


#
# -------- HEALTH CHECK --------
#

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Requirement Intelligence API is running"}


#
# -------- API ROUTES --------
#
# NOTE: router has NO prefix — so we add "/api" here
#

app.include_router(router, prefix="/api")
