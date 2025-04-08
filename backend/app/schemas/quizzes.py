from pydantic import BaseModel, ConfigDict
from app.schemas.books import BookOut

# quiz create schema
class QuizCreate(BaseModel):
    quiz_name: str
    points: int
    book_id: int
    
# quiz update schema
class QuizUpdate(BaseModel):
    quiz_name: str
    points: int
    book_id: int

# quiz out schema
class QuizOut(BaseModel):
    quiz_id: int
    quiz_name: str
    points: int
    book_id: int
    book: BookOut

    model_config = ConfigDict(from_attributes=True)



