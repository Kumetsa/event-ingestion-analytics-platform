"""
Service layer for event-related business logic.
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from app.repositories.event_repository import EventRepository
from app.schemas.event import EventCreate
from app.models.event import Event


class EventService:
    """Handles business logic related to event operations."""

    def __init__(self):
        self.event_repository = EventRepository()

    def create_event(self, db: Session, event_data: EventCreate) -> Event:
        """Create a new event record."""
        try:
            return self.event_repository.create_event(db=db, event_data=event_data)
        except IntegrityError as exc:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Event with event_id '{event_data.event_id}' already exists.",
            ) from exc

    def get_events(self,
                   db: Session,
                   event_type: str | None = None,
                   event_source: str | None = None
                   ) -> list[Event]:
        """Retrieve all events optionally filtered by type and source."""

        return self.event_repository.get_events(db=db, event_type=event_type, event_source=event_source)

    def get_event_by_event_id(self, db: Session, event_id: str) -> Event | None:
        """Retrieve a single event by its event_id."""
        return self.event_repository.get_event_by_event_id(db=db, event_id=event_id)