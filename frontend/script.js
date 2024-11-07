// frontend/script.js

async function fetchMessage() {
    const response = await fetch("http://localhost:5000/api/message");
    const data = await response.json();
    document.getElementById("message-container").innerText = data.message;
}

fetchMessage();
