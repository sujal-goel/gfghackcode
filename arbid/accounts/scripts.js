document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const emailInput = document.querySelector('input[type="email"]');
    const passwordInput = document.querySelector('input[type="password"]');
    const rememberCheckbox = document.querySelector('input[type="checkbox"]');
    const loginBox = document.querySelector('.login-box');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const email = emailInput.value;
        const password = passwordInput.value;
        const rememberMe = rememberCheckbox.checked;

        // You can add your authentication logic here
        // For now, we'll simulate a successful login
        if (email === "test@example.com" && password === "password") {
            displayMessage("Login successful!");
        } else {
            displayMessage("Invalid email or password.");
        }
        
        // Reset the form
        form.reset();
    });

    function displayMessage(message) {
        // Check if a message box already exists and remove it
        const existingMessageBox = document.querySelector('.message-box');
        if (existingMessageBox) {
            existingMessageBox.remove();
        }

        // Create a new message box
        const messageBox = document.createElement('div');
        messageBox.className = 'message-box';
        messageBox.textContent = message;

        // Append message box to the login box
        loginBox.appendChild(messageBox);

        // Remove message box after 3 seconds
        setTimeout(() => {
            messageBox.remove();
        }, 3000);
    }
});
