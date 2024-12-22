from src.models.settings import Base
from sqlalchemy import Column, Integer, String

class Events(Base):
    __tablename__ = 'events'
    __table_args__ = {'schema': 'nlw_events'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    details = Column(String(255))
    slug = Column(String(255), nullable=False) 
    maximum_attendees = Column(Integer)

    #Essa função tem como objetivo retornar uma representação da classe em forma de string
    #O método __repr__ é chamado quando a função print é chamada para um objeto
    def __repr__(self):
        return f"<Event(title={self.title}, details={self.details}, slug={self.slug}, maximum_attendees={self.maximum_attendees})>"
