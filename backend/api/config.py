import os
from pathlib import Path



# Base directory for file storage
BASE_DIR = Path(os.environ.get("STORAGE_PATH", "/tmp/uploads"))

# File type mapping
FILE_TYPE_MAPPING = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".webp": "Images",
    
    # PDFs
    ".pdf": "PDFs",
    
    # Documents
    ".doc": "Docs",
    ".docx": "Docs",
    ".txt": "Docs",
    ".rtf": "Docs",
    ".odt": "Docs",
    ".md": "Docs",
    
    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    
    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    
    # Video
    ".mp4": "Video",
    ".avi": "Video",
    ".mov": "Video",
    ".mkv": "Video",
    
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    
    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    ".cpp": "Code",
}