from sqlalchemy.orm import Session

from app.models.event import Event
from app.schemas.event import EventCreate


class EventRepository:
    def create_event(self, db: Session, event_data: EventCreate) -> Event:
        db_event = Event(
            event_id=event_data.event_id,
            event_type=event_data.event_type,
            event_source=event_data.event_source,
            user_id=event_data.user_id,
            session_id=event_data.session_id,
            occurred_at=event_data.occurred_at,
            amount=event_data.amount,
            currency=event_data.currency,
            metadata_json=event_data.metadata,
        )

        db.add(db_event)
        db.commit()
        db.refresh(db_event)

        return db_event
