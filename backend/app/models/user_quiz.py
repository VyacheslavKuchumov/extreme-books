from sqlalchemy import Column, BigInteger, Text, DateTime, Date, ForeignKey, Float, UUID
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.questions import Question

# class for quizzes
class UserQuiz(Base):
    __tablename__ = "user_quiz"

    user_quiz_id = Column(BigInteger, primary_key=True, index=True)
    user_uid = Column(UUID, ForeignKey("users.user_uid"), nullable=False)
    quiz_id = Column(BigInteger, ForeignKey("quizzes.quiz_id"), nullable=False)
    final_score = Column(Float, nullable=False)
    
    user = relationship("User", back_populates="user_quiz")
    quiz = relationship("Quiz", back_populates="user_quiz")





