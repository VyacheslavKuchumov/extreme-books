from pydantic import BaseModel, ConfigDict
from app.schemas.quizzes import QuizOut
from typing import Optional

# book create schema 
class BookCreate(BaseModel):
    title: str
    author: str
    img_url: str

# book update schema
class BookUpdate(BaseModel):
    title: str
    author: str
    img_url: str

# book out schema
class BookOut(BaseModel):
    book_id: int
    title: str
    author: str
    img_url: str
    
    quiz: Optional[list[QuizOut]] = None

    model_config = ConfigDict(from_attributes=True)


