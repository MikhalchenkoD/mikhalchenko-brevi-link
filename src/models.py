from typing import Dict, Any

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///urls.db')
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class URLMapping(Base):
    __tablename__ = 'urlmapping'
    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, nullable=False, unique=True)

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}