from sqlalchemy.orm import Session
from app.models.events import Event
from app.schemas.events import EventCreate, EventUpdate


# function for getting all events
def get_events(db: Session):
    return db.query(Event).all()


# function for creating a new event
def create_event(db: Session, event: EventCreate):
    db_event = Event(
        title=event.title,
        description=event.description,
        start_date=event.start_date,
        img_url=event.img_url
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# function for updating an existing event by id
def update_event(db: Session, event_id: int, event: EventUpdate):
    db_event = db.query(Event).filter(Event.event_id == event_id).first()
    db_event.title = event.title
    db_event.description = event.description
    db_event.start_date = event.start_date
    db_event.img_url = event.img_url
    db.commit()
    db.refresh(db_event)
    return db_event


# function for deleting an existing event by id
def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    db.delete(event)
    db.commit()
    return event

