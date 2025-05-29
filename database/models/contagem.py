from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.base import Base


class Contagem(Base):
    __tablename__ = "contagens"

    id = Column(Integer, primary_key=True, index=True)
    mob = Column(String, nullable=False)
    item = Column(String)
    count = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
