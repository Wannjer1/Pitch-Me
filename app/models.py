# creating model to define user data
from . import db 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True,unique=True)
    email = db.Column(db.String(200), index = True, unique=True)


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__='roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User{self.name}'