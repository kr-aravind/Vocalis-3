from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from .routers import script, video, impromptu, pronunciation, upload

app = FastAPI(title="Vocalis API", description="AI Communication & Public Speaking Coach API", version="1.0.0")

# Allow CORS from any origin for flexible local development and live servers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(script.router, prefix="/api")
app.include_router(video.router, prefix="/api/video")
app.include_router(impromptu.router, prefix="/api")
app.include_router(pronunciation.router, prefix="/api")
app.include_router(upload.router, prefix="/api")

# Serve static assets from project root
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
app.mount("/static", StaticFiles(directory=static_dir, html=False), name="static")

# Root endpoint serves index.html
@app.get("/")
async def read_root():
    index_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.html"))
    return FileResponse(index_path)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Vocalis Backend"}
