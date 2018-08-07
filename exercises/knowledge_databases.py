from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def add_article(topic, title, rating):
	artical_object = Knowledge( topic = topic, title = title, rating=rating)
	session.add(artical_object)
	session.commit()
def query_all_articles():
	articals = session.query(Knowledge).all()
	return(articals)

def query_article_by_topic(topic):
	artical = session.query(Knowledge).filter_by(topic = topic).all()
	return artical
def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()
	print("you deleted all the articals with the topic: ", topic)

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
	print("you deleted all articals ")
def query_article_by_rating(threshold):
	articles = session.query(Knowledge)	#. filter_by("rating <= {}".format(threshold)).all()
	for article in articles:
		if article.rating <=str(threshold):
			print(article)
def query_article_by_primary_key(key):
	artical = session.query(Knowledge).filter_by(primary_key = key).all()
	return artical

def edit_article_rating(updated_rating, article_title):
	articles = session.query(Knowledge).filter_by(title = article_title).all()
	for article in articles:
		article.rating = updated_rating
	session.commit()



#add_article("animals", "dogs", 8)
#add_article("animals", "cats", 6)
##delete_article_by_topic("animals")
##delete_all_articles()
##print(query_all_articles())
#query_article_by_rating(6)
print()
print()
print()
print()
##edit_article_rating(9, "cats")
#3delete_all_articles()
#print(query_article_by_topic("animals"))
query_article_by_rating(7)