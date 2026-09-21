import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load .env from project root (backend folder)
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env")))

# Load environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = None
try:
    if SUPABASE_URL and SUPABASE_KEY and "supabase.co" in SUPABASE_URL:
        from supabase import create_client, Client
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    logger.warning(f"Supabase client initialization bypassed: {e}")

# In-memory storage fallback
_local_db = {
    "script_results": [],
    "video_results": [],
    "pronunciation_results": []
}

def safe_db_insert(table_name: str, payload: dict):
    """Safely insert into Supabase or fallback to local in-memory store."""
    try:
        if supabase:
            res = supabase.table(table_name).insert(payload).execute()
            return res
    except Exception as e:
        logger.warning(f"Supabase table '{table_name}' insert bypassed ({e}); saving locally.")
    
    _local_db.setdefault(table_name, []).append(payload)
    return {"status": "saved_locally", "data": payload}

def upload_file(file_path: str, bucket: str = "storage") -> str:
    """Upload a local file to Supabase storage bucket or return local static URL.

    Args:
        file_path: Path to the local file.
        bucket: Supabase storage bucket name.
    Returns:
        Public or local URL of the file.
    """
    file_name = os.path.basename(file_path)
    try:
        if supabase:
            with open(file_path, "rb") as f:
                file_bytes = f.read()
            resp = supabase.storage.from_(bucket).upload(file_name, file_bytes)
            if not getattr(resp, "error", None):
                public_url = supabase.storage.from_(bucket).get_public_url(file_name)
                return public_url
    except Exception as e:
        logger.warning(f"Supabase storage upload bypassed ({e}); using local path.")

    # Return accessible relative storage URL
    return f"/static/backend/storage/{file_name}"
