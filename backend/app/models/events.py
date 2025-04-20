from sqlalchemy import Column, BigInteger, Text, DateTime, Date
from sqlalchemy.orm import relationship
from app.database import Base

# class for events
class Event(Base):
    __tablename__ = "events"

    event_id = Column(BigInteger, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=False)
    img_url = Column(Text, nullable=True)

    user_event = relationship(
        "UserEvent",
        uselist=True,
        back_populates="event",
        cascade="all, delete"
    )


