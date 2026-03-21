from sqlalchemy import Column, Integer, String, DateTime, JSON, Float
from datetime import datetime

from app.core.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String, unique=True, index=True, nullable=False)
    event_type = Column(String, index=True, nullable=False)
    event_source = Column(String, nullable=False)

    user_id = Column(String, nullable=True)
    session_id = Column(String, nullable=True)

    occurred_at = Column(DateTime, nullable=False)
    received_at = Column(DateTime, default=datetime.now)

    amount = Column(Float, nullable=True)
    currency = Column(String, nullable=True)

    metadata_json = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=datetime.now)
