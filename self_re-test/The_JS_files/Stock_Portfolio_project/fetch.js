// Example POST method implementation with an API key
async function postData(url = "", data = {}) {
    try {
        const response = await fetch(url, {
            method: "POST", // HTTP method (e.g., GET, POST, PUT, DELETE)
            mode: "cors", // CORS mode (can be "no-cors", "cors", "same-origin")
            cache: "no-cache", // Cache mode (e.g., "default", "no-cache", "reload", "force-cache", "only-if-cached")
            credentials: "same-origin", // Credentials mode (e.g., "include", "same-origin", "omit")
            headers: {
                "Content-Type": "application/json", // Specify content type
                "X-API-KEY": "your-api-key", // Include your API key
            },
            redirect: "follow", // Redirect mode (e.g., "manual", "follow", "error")
            referrerPolicy: "no-referrer", // Referrer policy (e.g., "no-referrer", "origin", "unsafe-url")
            body: JSON.stringify(data), // Convert data to JSON string
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const responseData = await response.json(); // Parse JSON response
        console.log(responseData); // Display the response data
        return responseData;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}

// Example usage: Send data to an API endpoint
const apiUrl = "https://api.example.com/endpoint"; // Replace with your API endpoint
const requestData = { key1: "value1", key2: "value2" }; // Replace with your data
postData(apiUrl, requestData);
