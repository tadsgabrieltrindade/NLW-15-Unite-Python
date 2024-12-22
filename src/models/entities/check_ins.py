from src.models.settings import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIn(Base):
    __tablename__ = 'check_ins'
    __table_args__ = {'schema': 'nlw_events'}

    Id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False,server_default=func.now())
    attendeeID = Column(Integer, ForeignKey('nlw_events.attendees.id'), nullable=False)

    def __repr__(self):
        return f"<CheckIn(created_at={self.created_at}, attendeeID={self.attendeeID})>"