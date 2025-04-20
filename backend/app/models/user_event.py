from sqlalchemy import Column, BigInteger, Text, DateTime, Date, ForeignKey, Float, UUID
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.questions import Question


# class for quizzes
class UserEvent(Base):
    __tablename__ = "user_event"

    user_event_id = Column(BigInteger, primary_key=True, index=True)
    user_uid = Column(UUID, ForeignKey("users.user_uid"), nullable=False)
    event_id = Column(BigInteger, ForeignKey("events.event_id"), nullable=False)
    
    user = relationship("User", back_populates="user_event")
    event = relationship("Event", back_populates="user_event")





