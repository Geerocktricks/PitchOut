from . import db

class User(db.Model):
    '''
    user class to help create new users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username} '

class Role(db.Model):
    '''
    Role class to give users different roles and access
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'