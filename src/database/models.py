from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    birthday = Column('b_day', DateTime, nullable=True)
    description = Column(String(250), nullable=True)



