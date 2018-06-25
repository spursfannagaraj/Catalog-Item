from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    @property
    def serialize(self):  # returns a serialized form of the instance variables
        return
        {
            "id": self.id,
            "name": self.name
        }


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        return
        {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category id": self.category_id
        }


# creates the DB file
engine = create_engine('sqlite:///catalogitem.db')


Base.metadata.create_all(engine)
