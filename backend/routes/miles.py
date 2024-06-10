from flask import Blueprint, request, jsonify
from backend.models import db, Miles

miles_bp = Blueprint('miles', __name__)

@miles_bp.route('/add', methods=['POST'])
def add_miles():
    data = request.get_json()
    new_miles = Miles(
        passenger_name=data['passenger_name'],
        miles=data['miles']
    )
    db.session.add(new_miles)
    db.session.commit()
    return jsonify({"message": "Miles added successfully"}), 201

@miles_bp.route('/list', methods=['GET'])
def list_miles():
    miles_records = Miles.query.all()
    result = [{"id": record.id, "passenger_name": record.passenger_name, "miles": record.miles} for record in miles_records]
    return jsonify(result), 200
