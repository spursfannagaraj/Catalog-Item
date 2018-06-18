from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__= 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

class Item(Base):
    __tablename__='item'
    id = Column(Integer,primary_key= True)
    title = Column(String(30), nullable = False)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category=relationship(Category)



engine = create_engine('sqlite:///catalogitem.db')


Base.metadata.create_all(engine)