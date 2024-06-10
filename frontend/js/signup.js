document.getElementById('signupForm').addEventListener('submit', function(e) {
    e.preventDefault();
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;

    fetch('/miles/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: name, email: email }),
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('signupResult');
        resultDiv.textContent = 'Signup successful!';
    })
    .catch(error => console.error('Error:', error));
});
