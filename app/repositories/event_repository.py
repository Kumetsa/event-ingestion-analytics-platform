from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from app.models.event import Event
from app.schemas.event import EventCreate


class EventRepository:
    def create_event(self, db: Session, event_data: EventCreate) -> Event:
        """Create and persist a new event record."""
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

        try:
            db.commit()
            db.refresh(db_event)
        except IntegrityError:
            db.rollback()
            raise

        return db_event

    def get_events(self,
                   db: Session,
                   event_type: str | None = None,
                   event_source: str | None = None
                   ) -> list[Event]:
        """Return events, optionally filtered by type and source"""

        query = select(Event)

        if event_type:
            query = query.where(Event.event_type == event_type)

        if event_source:
            query = query.where(Event.event_source == event_source)

        query = query.order_by(Event.occurred_at.desc())

        return list(db.scalars(query).all())

    def get_event_by_event_id(self,
                              db: Session,
                              event_id: str,
                              ) -> Event | None:
        """Return a single event by event_id"""
        query = select(Event).where(Event.event_id == event_id)
        return db.scalar(query)