from sqlalchemy import Column, Integer, String, JSON, Boolean
from app.database import Base

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    slug = Column(String, unique=True)
    title = Column(String)
    description = Column(String)
    questions = Column(JSON)  
    is_active = Column(Boolean, default=True)