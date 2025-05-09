from fastapi import APIRouter
import uuid
from fastapi import File, UploadFile, HTTPException
from typing import List
from fastapi.responses import FileResponse
from config import BASE_DIR 
from models import FileOrganizeResponse
from utils import organize_uploaded_files
from logging_config import logger

router = APIRouter()

@router.post("/files", response_model=FileOrganizeResponse)
async def upload_files(files: List[UploadFile] = File(...)):
    """Upload and organize multiple files."""
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")
    
    # Generate unique session ID
    session_id = str(uuid.uuid4())
    
    # Organize the files
    result = organize_uploaded_files(session_id, files)
    
    # Generate download URL
    download_url = f"/download/{session_id}"
    
    return FileOrganizeResponse(
        session_id=session_id,
        download_url=download_url,
        preview=result["preview"],
        organized_files=result["organized_files"]
    )

@router.get("/download/{session_id}")
async def download_zip(session_id: str):
    """Download the organized files as a ZIP archive."""
    # Validate session ID format to prevent path traversal
    try:
        uuid_obj = uuid.UUID(session_id)
        logger.info(f"Downloading organized files for session: {session_id}")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid session ID")
    
    zip_path = BASE_DIR / session_id / "organized.zip"
    
    if not zip_path.exists():
        raise HTTPException(status_code=404, detail="ZIP file not found")
    
    return FileResponse(
        path=zip_path,
        filename="organized_files.zip",
        media_type="application/zip"
    )

@router.get("/")
async def root():
    """Root endpoint for health check."""
    return {"message": "File Organizer API is running"}
