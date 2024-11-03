from sqlalchemy import Column, Integer, String, VARCHAR
from .db import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key= True, nullable= False, autoincrement= True)
    name = Column(String(100), index = True)
    description = Column(String(500), index = True)