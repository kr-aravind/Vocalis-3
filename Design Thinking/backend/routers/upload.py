from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import uuid
from ..utils.supabase_client import upload_file

router = APIRouter()

STORAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "storage"))
os.makedirs(STORAGE_DIR, exist_ok=True)

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    """Upload a file, store locally and/or to Supabase, and return its access URL."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    ext = os.path.splitext(file.filename)[1]
    unique_name = f"{uuid.uuid4().hex}{ext}"
    local_path = os.path.join(STORAGE_DIR, unique_name)
    
    with open(local_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        url = upload_file(local_path)
    except Exception:
        url = f"/static/backend/storage/{unique_name}"
        
    return {
        "success": True,
        "filename": file.filename,
        "url": url
    }
