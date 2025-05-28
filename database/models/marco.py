from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.base import Base


class Marco(Base):
    __tablename__ = "marcos"

    id = Column(Integer, primary_key=True, index=True)
    mob = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
    timestamp_inicio = Column(DateTime, nullable=False, default=datetime.utcnow)
    timestamp_fim = Column(DateTime, nullable=True)
