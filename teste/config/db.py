from . import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import dotenv

environment = dotenv.dotenv_values(".env")
engine = create_engine(environment['DATABASE_CONNECTION_STRING'], echo=False)

Base = declarative_base()