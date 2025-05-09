import os
import shutil
from datetime import datetime, timedelta
from logging_config import logger
from typing import List, Dict 
from pathlib import Path
import zipfile
from fastapi import UploadFile
import asyncio
from config import BASE_DIR, FILE_TYPE_MAPPING


# Ensure directories exist
def ensure_directories():
    BASE_DIR.mkdir(exist_ok=True, parents=True)

# Remove all old files (1 hour old)
async def cleanup_old_files():
    while True:
        try:
            now = datetime.now()
            cutoff = now - timedelta(hours=1)
            
            for session_dir in BASE_DIR.iterdir():
                if not session_dir.is_dir():
                    continue
                    
                # Check creation time of directory
                creation_time = datetime.fromtimestamp(session_dir.stat().st_ctime)
                if creation_time < cutoff:
                    logger.info(f"Cleaning up old session: {session_dir}")
                    shutil.rmtree(session_dir, ignore_errors=True)
            
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
        
        # Run cleanup every 15 minutes
        await asyncio.sleep(15 * 60)


def get_file_category(file_name: str) -> str:
    """Determine the category based on file extension."""
    suffix = Path(file_name).suffix.lower()
    return FILE_TYPE_MAPPING.get(suffix, "Others")

def organize_uploaded_files(session_id: str, files: List[UploadFile]) -> Dict:
    """
    Organizes uploaded files into categories and creates a zip file.
    Returns information about the organization structure.
    """
    session_dir = BASE_DIR / session_id
    original_dir = session_dir / "original"
    organized_dir = session_dir / "organized"
    
    # Create session directories
    original_dir.mkdir(exist_ok=True, parents=True)
    organized_dir.mkdir(exist_ok=True, parents=True)
    
    # Structure to track organized files
    organization_structure = {}
    all_organized_files = []
    
    # Process each file
    for file in files:
        # Save original file
        file_path = original_dir / file.filename
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
        # Determine category and create folder if needed
        category = get_file_category(file.filename)
        category_dir = organized_dir / category
        category_dir.mkdir(exist_ok=True)
        
        # Copy file to the category directory
        dest_path = category_dir / file.filename
        shutil.copy2(file_path, dest_path)
        
        # Track the organization
        if category not in organization_structure:
            organization_structure[category] = []
        organization_structure[category].append(file.filename)
        all_organized_files.append(f"{category}/{file.filename}")
    
    # Create a zip file of the organized directory
    zip_path = session_dir / "organized.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(organized_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, organized_dir)
                zipf.write(file_path, arcname=arcname)
    
    # Convert organization structure to the format expected by the frontend
    preview = [{"folder": folder, "files": files} for folder, files in organization_structure.items()]
    
    return {
        "preview": preview,
        "organized_files": all_organized_files
    }
