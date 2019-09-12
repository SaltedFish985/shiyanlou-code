from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    score = Column(Float)
    mean_price = Column(Integer)