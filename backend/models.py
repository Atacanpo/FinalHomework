from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    passenger_name = db.Column(db.String(50), nullable=False)

class Miles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    passenger_name = db.Column(db.String(50), nullable=False)
    miles = db.Column(db.Integer, nullable=False)
