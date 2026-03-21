from fastapi import APIRouter, Depends, status
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
