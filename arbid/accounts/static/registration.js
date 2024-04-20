document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const usernameInput = document.querySelector('input[type="text"][placeholder="Username"]');
    const companyNameInput = document.querySelector('input[type="text"][placeholder="Company Name"]');
    const emailInput = document.querySelector('input[type="email"]');
    const passwordInput = document.querySelector('input[type="password"]');
    const loginBox = document.querySelector('.login-box');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const username = usernameInput.value;
        const companyName = companyNameInput.value;
        const email = emailInput.value;
        const password = passwordInput.value;

        // You can add your registration logic here
        // For now, we'll simulate a successful registration
        displayMessage("Registration successful! Welcome, " + username + "!");

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
