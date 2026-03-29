"""
API routes for creating event records.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.event import EventCreate, EventResponse
from app.services.event_service import EventService

router = APIRouter(prefix="/events", tags=["events"])

event_service = EventService()


@router.post("", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event_endpoint(
    event: EventCreate,
    db: Session = Depends(get_db),
) -> EventResponse:
    created_event = event_service.create_event(db=db, event_data=event)
    return EventResponse.model_validate(created_event)


@router.get("", response_model=list[EventResponse], status_code=status.HTTP_200_OK)
def get_events_endpoint(
        event_type: str | None = Query(default=None),
        event_source: str | None = Query(default=None),
        db: Session = Depends(get_db),
        limit: int = Query(default=100, ge=1, le=500),
        offset: int = Query(default=0, ge=0),
) -> list[EventResponse]:
    """Return events with optional filtering and pagination."""

    events = event_service.get_events(db=db,
                                      event_type=event_type,
                                      event_source=event_source,
                                      limit=limit,
                                      offset=offset,
    )
    return [EventResponse.model_validate(event) for event in events]


@router.get("/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
def get_event_by_event_id_endpoint(
        event_id: str,
        db: Session = Depends(get_db),
) -> EventResponse:
    """Returns a single event by its event_id."""
    event = event_service.get_event_by_event_id(db=db, event_id=event_id)

    if event is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with event_id '{event_id}' was not found.",
        )

    return EventResponse.model_validate(event)