from pydantic import BaseModel, ConfigDict
from app.schemas.answers import AnswerOut
from typing import Optional



# question create schema
class QuestionCreate(BaseModel):
    question_text: str
    quiz_id: int
    
# question update schema
class QuestionUpdate(BaseModel):
    question_text: str
    quiz_id: int

# question out schema
class QuestionOut(BaseModel):
    question_id: int
    question_text: str
    quiz_id: int
    
    answer: Optional[list[AnswerOut]] = None

    model_config = ConfigDict(from_attributes=True)

