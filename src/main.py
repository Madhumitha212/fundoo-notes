from fastapi import FastAPI
from src.config.database_conn import engine
from src.models.user_model import Base
from src.router.user_route import router
from src.config.logging_config import *

logger = setup_logger()
app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(router)
