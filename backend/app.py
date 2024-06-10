from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kullanici:sifre@localhost/veritabani'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'

db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)

def create_app():
    from backend.routes import flight_bp, ticket_bp, miles_bp

    app.register_blueprint(flight_bp, url_prefix='/flights')
    app.register_blueprint(ticket_bp, url_prefix='/tickets')
    app.register_blueprint(miles_bp, url_prefix='/miles')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
