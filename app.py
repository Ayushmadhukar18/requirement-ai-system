# Import core FastAPI framework
from fastapi import FastAPI, Request

# Used when returning HTML responses instead of JSON
from fastapi.responses import HTMLResponse

# Used to serve static files like CSS, JS, images
from fastapi.staticfiles import StaticFiles

# Jinja2 template engine for rendering HTML pages
from fastapi.templating import Jinja2Templates

# Import API routes defined in api/routes.py
from api.routes import router


# Create FastAPI application instance
app = FastAPI(
    title="Requirement Intelligence Agent",
    version="1.0"
)


# Mount static directory so frontend assets can be served
# Example: /static/style.css
app.mount("/static", StaticFiles(directory="static"), name="static")


# Configure Jinja2 template directory
# This folder contains HTML files for the UI dashboard
templates = Jinja2Templates(directory="templates")


# Root route - loads the dashboard UI
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """
    Serves the main dashboard page.
    Renders index.html using the Jinja2 template engine.
    """
    return templates.TemplateResponse("index.html", {"request": request})


# Health check endpoint
# Useful for monitoring and container orchestration systems
@app.get("/health")
async def health_check():
    """
    Simple API endpoint used to verify that the service is running.
    Often used by load balancers, Docker, or Kubernetes health checks.
    """
    return {
        "status": "ok",
        "message": "Requirement Intelligence API is running"
    }


# Register API routes under /api prefix
# Example endpoint: /api/analyze
app.include_router(router, prefix="/api")