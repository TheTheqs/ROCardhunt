from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.base import Base
from sqlalchemy import Numeric


class Contagem(Base):
    __tablename__ = "contagens"

    id = Column(Integer, primary_key=True, index=True)
    mob = Column(String, nullable=False)
    item = Column(String)
    chance = Column(Numeric(5, 2), nullable=False, default=0.0)
    count = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
