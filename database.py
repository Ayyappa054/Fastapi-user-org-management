from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Database URL
DATABASE_URL = "mysql+mysqlconnector://root:Ayyappa%400505@localhost:3306/demo"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# SQLAlchemy session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  
