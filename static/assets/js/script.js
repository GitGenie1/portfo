document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;
    
    if(name && email && message) {
        alert("Message sent! We'll get back to you soon.");
        // Additional AJAX code to send data to server could be added here
    } else {
        alert("Please fill out all fields.");
    }
});
