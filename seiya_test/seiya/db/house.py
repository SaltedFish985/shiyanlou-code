from sqlalchemy import Column, Integer, String
from .base import Base

class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    housing_estate = Column(String(64), index=True)
    area = Column(Integer)
    orientations = Column(String(64), index=True)
    apartment = Column(String(64), index=True)
    rent = Column(Integer)