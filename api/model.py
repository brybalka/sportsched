from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class UFCEventModel(Base, dict):
    __tablename__ = 'ufc_event'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    status = Column(String)

    def __repr__(self):
        return "UFCEventModel(id ='{}', name='{}', date='{}', status='{}')>" \
            .format(self.id, self.name, self.date, self.status)
