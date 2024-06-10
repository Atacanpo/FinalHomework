from flask import Blueprint, request, jsonify
from backend.models import db, Flight

flight_bp = Blueprint('flights', __name__)

@flight_bp.route('/add', methods=['POST'])
def add_flight():
    data = request.get_json()
    new_flight = Flight(
        origin=data['origin'],
        destination=data['destination'],
        date=data['date'],
        capacity=data['capacity']
    )
    db.session.add(new_flight)
    db.session.commit()
    return jsonify({"message": "Flight added successfully"}), 201

@flight_bp.route('/search', methods=['GET'])
def search_flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    flights = Flight.query.filter_by(origin=origin, destination=destination).all()
    result = [{"id": flight.id, "origin": flight.origin, "destination": flight.destination, "date": flight.date, "capacity": flight.capacity} for flight in flights]
    return jsonify(result), 200
