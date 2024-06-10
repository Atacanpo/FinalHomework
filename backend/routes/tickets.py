from flask import Blueprint, request, jsonify
from backend.models import db, Ticket

ticket_bp = Blueprint('tickets', __name__)

@ticket_bp.route('/add', methods=['POST'])
def add_ticket():
    data = request.get_json()
    new_ticket = Ticket(
        flight_id=data['flight_id'],
        passenger_name=data['passenger_name']
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({"message": "Ticket added successfully"}), 201

@ticket_bp.route('/list', methods=['GET'])
def list_tickets():
    tickets = Ticket.query.all()
    result = [{"id": ticket.id, "flight_id": ticket.flight_id, "passenger_name": ticket.passenger_name} for ticket in tickets]
    return jsonify(result), 200
