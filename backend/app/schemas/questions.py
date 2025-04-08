from pydantic import BaseModel, ConfigDict
# from app.schemas.books import BookOut



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

    model_config = ConfigDict(from_attributes=True)

