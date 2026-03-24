from sqlalchemy import Column, Integer, String, Boolean
from config.database_conn import Base
 
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String(100))
    email = Column(String(150), unique=True, nullable = False)
    password = Column(String(200), nullable = False)
    contact_no = Column(String(15), nullable=True)
    is_active = Column(Boolean, default=False)