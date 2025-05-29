from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.base import Base
from database.models.contagem import Contagem


class Marco(Base):
    __tablename__ = "marcos"

    id = Column(Integer, primary_key=True, index=True)
    mob = Column(String, nullable=False)
    item = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
    timestamp_inicio = Column(DateTime, nullable=False)
    timestamp_fim = Column(DateTime, nullable=True)

    def create(self, contagem: Contagem):
        new_marco = Marco()
        new_marco.mob = contagem.mob
        new_marco.item = contagem.item
        new_marco.count = contagem.count
        new_marco.timestamp_inicio = contagem.timestamp
        new_marco.timestamp_fim = datetime.utcnow()
        return new_marco
