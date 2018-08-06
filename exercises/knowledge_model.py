from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "knowledge"
	number = Column(Integer, primary_key=True)
	topic = Column(String)
	title = Column(String)
	rating = Column(String)

	def __repr__(self):
    	if self.rating >=7:
		   return ("If you want to learn about: {} "
               ", you should look at the Wikipedia article called: {} "
               "We gave this article a rating of {}").format(
                    self.topic, self.title, self.rating)
	   	else:
			   return ("If you want to learn about: {} "
               ", you should look at the Wikipedia article called: {} "
               "Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!.").format(
                    self.topic, self.title)

	