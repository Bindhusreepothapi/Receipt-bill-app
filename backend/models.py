# --- backend/models.py ---
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()
class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    merchant = Column(String, index=True)
    date = Column(String)
    total = Column(Float)
    items = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)