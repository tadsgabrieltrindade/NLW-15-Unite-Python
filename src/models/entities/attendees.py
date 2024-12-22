from src.models.settings import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.sql import func


class Attendees(Base):
    __tablename__ = 'attendees'
    __table_args__ = {'schema': 'nlw_events'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    event_id = Column(Integer, ForeignKey('nlw_events.events.id'))
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    #Fazendo uma analogia com C# ou Java, o __repr__ é como se fosse o ToString()
    def __repr__(self):
        return f"<Attendees(id={self.id}, name={self.name}, email={self.email}, event_id={self.event_id}, created_at={self.created_at})>"