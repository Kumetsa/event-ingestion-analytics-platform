from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class EventCreate(BaseModel):
    event_id: str = Field(..., min_length=1, max_length=100)
    event_type: str = Field(..., min_length=1, max_length=100)
    event_source: str = Field(..., min_length=1, max_length=100)

    user_id: str | None = Field(default=None, max_length=100)
    session_id: str | None = Field(default=None, max_length=100)

    occurred_at: datetime

    amount: float | None = Field(default=None)
    currency: str | None = Field(default=None, max_length=10)

    metadata: dict[str, Any] | None = Field(default=None)


class EventResponse(BaseModel):
    id: int
    event_id: str
    event_type: str
    event_source: str
    user_id: str | None
    session_id: str | None
    occurred_at: datetime
    received_at: datetime
    amount: float | None
    currency: str | None
    metadata_json: dict[str, Any] | None

    class Config:
        from_attributes = True
