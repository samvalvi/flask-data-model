from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username":self.username,
            "first_name":self.first_name,
            "last_name":self.last_name
        }

class Planet(db.Model):
    __tablename__ = 'Planet'
    # Here we define columns for the table planet
    # Notice that each column is also a normal Python instance attribute.
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    climate= db.Column(db.String(250), nullable=False)
    population= db.Column(db.Integer, nullable=False)
    orbital_period= db.Column(db.Integer, nullable=False)
    rotation_period= db.Column(db.Integer, nullable=False)
    diameter= db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate" : self.climate,
            "population" : self.population,
            "orbital_period" : self.orbital_period,
            "diameter": self.diameter
        }

class Character(db.Model):
    __tablename__ = 'Character'
    # Here we define columns for the table character
    # Notice that each column is also a normal Python instance attribute.
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    birth= db.Column(db.String(250), nullable=False)
    gender= db.Column(db.String(250), nullable=False)
    height= db.Column(db.Integer, nullable=False)
    skin= db.Column(db.String(250), nullable=False)
    eye= db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth" : self.birth,
            "gender" : self.gender,
            "height" : self.height,
            "skin" : self.skin,
            "eye" : self.eye
        }

class Favorite(db.Model):
    __tablename__ = 'Favorite'
    # Here we define columns for the table favorite
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('User.id'))
    planet_id= db.Column(db.Integer, db.ForeignKey('Planet.id'))
    character_id= db.Column(db.Integer, db.ForeignKey('Character.id'))
    user = db.relationship(User)
    planet = db.relationship(Planet)
    character = db.relationship(Character)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }