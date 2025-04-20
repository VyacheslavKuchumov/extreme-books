from sqlalchemy.orm import Session
from app.models.user_event import UserEvent
from app.schemas.user_event import UserEventCreate, UserEventUpdate




# function for getting a user event by user uid
def get_user_event_by_uid(db: Session, user_uid: str):
    return db.query(UserEvent).filter(UserEvent.user_uid == user_uid).all()


# function for getting a user events by event id
def get_user_event_by_event_id(db: Session, event_id: int):
    return db.query(UserEvent).filter(UserEvent.event_id == event_id).all()

# function for creating a new user event
def create_user_event(db: Session, user_event: UserEventCreate):
    db_user_event = UserEvent(
        user_uid=user_event.user_uid,
        event_id=user_event.event_id
    )
    db.add(db_user_event)
    db.commit()
    db.refresh(db_user_event)
    return db_user_event

# function for updating an existing user event by id
def update_user_event(db: Session, user_event_id: int, user_event: UserEventUpdate):
    db_user_event = db.query(UserEvent).filter(UserEvent.user_event_id == user_event_id).first()
    db_user_event.user_uid = user_event.user_uid
    db_user_event.event_id = user_event.event_id
    db.commit()
    db.refresh(db_user_event)
    return db_user_event

# function for deleting an existing user event by id
def delete_user_event(db: Session, user_event_id: int):
    user_event = db.query(UserEvent).filter(UserEvent.user_event_id == user_event_id).first()
    db.delete(user_event)
    db.commit()
    return user_event
