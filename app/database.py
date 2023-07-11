# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Carregar o arquivo .env
load_dotenv()

# Ler a configuração do banco de dados
production_db_config = os.getenv('PRODUCTION_DB_URL')
staging_db_config = os.getenv('STAGING_DB_URL')
model_production = os.getenv('MODEL_PRODUCTION').lower() == 'true'
clear_db = os.getenv('CLEAR_DB').lower() == 'true'

# Decidir qual configuração usar (você pode implementar essa lógica como quiser)
db_config = production_db_config if model_production else staging_db_config

# Criar a engine de conexão
engine = create_engine(db_config, echo=True)

# Criar a sessão do banco de dados
Session = sessionmaker(bind=engine)

# Base declarativa para criação de Models
Base = declarative_base()

def get_db_params():
    return clear_db, engine
