from sqlalchemy import Column, Integer, String, VARCHAR
from .db import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), index = True)