from pydantic import BaseModel, ConfigDict

from app.schemas.events import EventOut
from app.schemas.user import UserOut
from typing import Optional
from uuid import UUID



# user event create schema
class UserEventCreate(BaseModel):
    user_uid: UUID
    event_id: int
    
# user event update schema
class UserEventUpdate(BaseModel):
    user_uid: UUID
    event_id: int

# user event out schema
class UserEventOut(BaseModel):
    user_event_id: int
    user_uid: UUID
    event_id: int
    
    user: UserOut
    event: EventOut
    
    model_config = ConfigDict(from_attributes=True)



