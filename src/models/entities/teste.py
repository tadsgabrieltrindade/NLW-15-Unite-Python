from src.models.settings import Base
from sqlalchemy import Column, Integer, String

class Teste(Base):
    __tablename__ = 'tbl_teste'
    __table_args__ = {'schema': 'dbo'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    teste = Column(String(5), nullable=True)
