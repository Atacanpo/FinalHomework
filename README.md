# Airline Ticket Booking Application

This project is a web application for purchasing airline tickets. It features a Flask-based backend and an HTML/CSS/JavaScript frontend. The application is containerized using Docker and utilizes Alembic for database migrations. The backend is configured to use PostgreSQL.

- [![Video Link]](https://drive.google.com/file/d/1n8APcIrjyu6TXcJWEa2QF8-eR_lTGqIZ/view?usp=sharing)
![ER Diagram](https://github.com/Atacanpo/FinalHomework/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-06-10%20182922.png)


## Installation

### Prerequisites

- Python 3.x
- Docker
- PostgreSQL

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/airline-ticket-booking.git
    cd airline-ticket-booking
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure PostgreSQL:**

    Update the `SQLALCHEMY_DATABASE_URI` in `app.py` and `sqlalchemy.url` in `alembic.ini` with your PostgreSQL credentials.

5. **Initialize the database:**

    ```sh
    alembic upgrade head
    ```

## Usage

### Running the Application

1. **Start the Flask application:**

    ```sh
    flask run
    ```

2. **Access the application:**

    Open your web browser and go to `http://localhost:5000`.

### Running with Docker

1. **Build the Docker image:**

    ```sh
    docker build -t airline-ticket-app .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 5000:5000 airline-ticket-app
    ```

