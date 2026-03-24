from sqlalchemy import Column, Integer, String, ForeignKey
from src.config.database_conn import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(String(500), nullable=False)
