from pydantic import BaseModel, ConfigDict
from app.schemas.books import BookOut

# quiz create schema
class QuizCreate(BaseModel):
    points: int
    book_id: int
    
# quiz update schema
class QuizUpdate(BaseModel):
    points: int
    book_id: int

# quiz out schema
class QuizOut(BaseModel):
    quiz_id: int
    points: int
    book_id: int
    book: BookOut

    model_config = ConfigDict(from_attributes=True)



