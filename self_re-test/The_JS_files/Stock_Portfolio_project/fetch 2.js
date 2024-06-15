// Example GET method implementation
async function getData(url = "") {
    try {
        const response = await fetch(url, {
            method: "GET", // HTTP method (GET in this case)
            mode: "cors", // CORS mode (can be "no-cors", "cors", "same-origin")
            cache: "no-cache", // Cache mode (e.g., "default", "no-cache", "reload", "force-cache", "only-if-cached")
            credentials: "same-origin", // Credentials mode (e.g., "include", "same-origin", "omit")
            headers: {
                "Content-Type": "application/json", // Specify content type (not needed for GET requests)
            },
            redirect: "follow", // Redirect mode (e.g., "manual", "follow", "error")
            referrerPolicy: "no-referrer", // Referrer policy (e.g., "no-referrer", "origin", "unsafe-url")
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

// Example usage: Retrieve data from an API endpoint
const apiUrl = "https://api.example.com/data"; // Replace with your API endpoint
getData(apiUrl);
