from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from contextlib import asynccontextmanager
from routes import router
from utils import ensure_directories, cleanup_old_files
from logging_config import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application")
    ensure_directories()
    asyncio.create_task(cleanup_old_files())
    yield
    


app = FastAPI(title="File Organizer API", lifespan=lifespan)

# Allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5000)