from sqlalchemy import create_engine, Column, Integer, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:12322585207@localhost:5432/postgres"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

Base.metadata.create_all(engine)