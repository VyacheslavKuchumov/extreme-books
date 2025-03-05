from pydantic import BaseModel, ConfigDict
from datetime import date


# event create schema
class EventCreate(BaseModel):
    title: str
    description: str
    start_date: date
    img_url: str
    
# event update schema
class EventUpdate(BaseModel):
    title: str
    description: str
    start_date: date
    img_url: str

# event out schema
class EventOut(BaseModel):
    event_id: int
    title: str
    description: str
    start_date: date
    img_url: str

    model_config = ConfigDict(from_attributes=True)

