import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from database.base import Base

# IMPORTA AQUI todos os modelos pra registrar no metadata
from database.models.contagem import Contagem
from database.models.marco import Marco

os.makedirs("data", exist_ok=True)

DATABASE_URL = "sqlite:///data/cardhunt.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("[DB] Banco de dados inicializado.")
