from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Route for the root URL
@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    return FileResponse("/frontend/templates/index.html")

# Example health check route
@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}