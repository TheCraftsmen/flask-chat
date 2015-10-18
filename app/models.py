from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Chat(db.Model):

	__tablename__ = "chat"
	
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String, nullable=False)
	message = db.Column(db.String, nullable=False)

	def __init__(self, user, message):
		self.user = user
		self.message = message

	def __repr__(self):
		pass
