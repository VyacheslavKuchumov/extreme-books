from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_event import UserEventCreate, UserEventUpdate, UserEventOut
from app.controllers.user_event import create_user_event, get_user_event_by_uid, get_user_event_by_event_id, update_user_event, delete_user_event

from app.database import get_db

router = APIRouter()

# get user events for user uid
@router.get("/user/{user_uid}", response_model=list[UserEventOut])
def get_user_events(user_uid: str, db: Session = Depends(get_db)):
    return get_user_event_by_uid(db, user_uid)


# get user events for event id
@router.get("/event/{event_id}", response_model=list[UserEventOut])
def get_user_events(event_id: int, db: Session = Depends(get_db)):
    return get_user_event_by_event_id(db, event_id)

# create a new user event
@router.post("/", response_model=UserEventOut)
def create_user_event_route(user_event: UserEventCreate, db: Session = Depends(get_db)):
    return create_user_event(db, user_event)


# update an existing user event by id
@router.put("/{user_event_id}", response_model=UserEventOut)
def update_user_event_route(user_event_id: int, user_event: UserEventUpdate, db: Session = Depends(get_db)):
    return update_user_event(db, user_event_id, user_event)


# delete an existing user event by id
@router.delete("/{user_event_id}", response_model=UserEventOut)
def delete_user_event_route(user_event_id: int, db: Session = Depends(get_db)):
    return delete_user_event(db, user_event_id)