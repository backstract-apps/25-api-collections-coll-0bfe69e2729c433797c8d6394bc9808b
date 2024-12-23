from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BUser(Base):
    __tablename__ = 'b_user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, primary_key=False)

