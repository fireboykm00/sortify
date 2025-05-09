from pydantic import BaseModel
from typing import List, Dict

class FileOrganizeResponse(BaseModel):
    session_id: str
    download_url: str
    preview: List[Dict]
    organized_files: List[str]