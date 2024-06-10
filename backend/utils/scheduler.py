from apscheduler.schedulers.background import BackgroundScheduler
from app import db
from models import MilesSmilesMember, Ticket
from utils.email_utils import send_email

def update_miles_points():
    tickets = Ticket.query.all()
    for ticket in tickets:
        if ticket.miles_member_id:
            member = MilesSmilesMember.query.get(ticket.miles_member_id)
            if member:
                member.miles_points += 10  # Her uçuş için 10 puan ekleme
                db.session.commit()

def send_welcome_emails():
    members = MilesSmilesMember.query.filter_by(miles_points=0).all()
    for member in members:
        send_email(member.email, "Welcome to Miles&Smiles", "Welcome to Miles&Smiles Program!")

scheduler = BackgroundScheduler()
scheduler.add_job(update_miles_points, 'interval', days=1)
scheduler.add_job(send_welcome_emails, 'interval', days=1)
scheduler.start()
