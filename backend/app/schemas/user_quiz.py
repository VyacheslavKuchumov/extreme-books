from pydantic import BaseModel, ConfigDict

from app.schemas.quizzes import QuizOut
from app.schemas.user import UserOut
from typing import Optional
from uuid import UUID


# user quiz create schema
class UserQuizCreate(BaseModel):
    user_uid: UUID
    quiz_id: int
    final_score: float
    
# user quiz update schema
class UserQuizUpdate(BaseModel):
    user_uid: UUID
    quiz_id: int
    final_score: float
    
# user quiz out schema
class UserQuizOut(BaseModel):
    user_quiz_id: int
    user_uid: UUID
    quiz_id: int
    final_score: float
    
    user: UserOut
    quiz: QuizOut
    
    model_config = ConfigDict(from_attributes=True)