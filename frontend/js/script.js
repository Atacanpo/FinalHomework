document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    let origin = document.getElementById('origin').value;
    let destination = document.getElementById('destination').value;
    
    fetch(`/flights/search?origin=${origin}&destination=${destination}`)
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            data.forEach(flight => {
                let flightInfo = document.createElement('div');
                flightInfo.textContent = `Flight from ${flight.origin} to ${flight.destination} on ${flight.date}`;
                resultsDiv.appendChild(flightInfo);
            });
        })
        .catch(error => console.error('Error:', error));
});
