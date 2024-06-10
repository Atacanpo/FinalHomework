document.getElementById('buyForm').addEventListener('submit', function(e) {
    e.preventDefault();
    let flightId = document.getElementById('flight_id').value;
    let passengerName = document.getElementById('passenger_name').value;
    let passengerEmail = document.getElementById('passenger_email').value;
    let numberOfPassengers = document.getElementById('number_of_passengers').value;
    let milesMemberId = document.getElementById('miles_member_id').value || null;

    fetch('/tickets/buy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            flight_id: flightId,
            passenger_name: passengerName,
            passenger_email: passengerEmail,
            number_of_passengers: numberOfPassengers,
            miles_member_id: milesMemberId,
        }),
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('buyResult');
        resultDiv.textContent = 'Tickets bought successfully!';
    })
    .catch(error => console.error('Error:', error));
});
