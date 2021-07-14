from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLACHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLACHEMY_DATABASE_URL,connect_args ={"check_same_thread":False})


SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)


Base = declarative_base()