from fastapi import FastAPI
from src.config.database_conn import *
from src.router.user_route import router as user_router
from src.router.notes_route import router as notes_router
from src.config.logging_config import *

logger = setup_logger()
app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(user_router)
app.include_router(notes_router)
