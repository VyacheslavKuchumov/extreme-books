from sqlalchemy import Column, BigInteger, Text, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# class for quizzes
class Quiz(Base):
    __tablename__ = "quizzes"

    quiz_id = Column(BigInteger, primary_key=True, index=True)
    points = Column(BigInteger, nullable=False)
    book_id = Column(BigInteger, ForeignKey("books.book_id"), nullable=False)
    
    book = relationship("Book", back_populates="quizzes")
    # questions = relationship("Question", back_populates="quiz")




