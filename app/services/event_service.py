from sqlalchemy.orm import Session

from app.repositories.event_repository import EventRepository
from app.schemas.event import EventCreate
from app.models.event import Event


class EventService:
    def __init__(self):
        self.event_repository = EventRepository()

    def create_event(self, db: Session, event_data: EventCreate) -> Event:
        return self.event_repository.create_event(db=db, event_data=event_data)