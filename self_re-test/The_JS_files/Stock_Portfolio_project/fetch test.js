// https://fcsapi.com/api-v3/forex/latest?id=1&access_key=API_KEY

// Example GET method implementation
const display = document.getElementById("display")

async function getNgn_Usd_Rate(url = `https://api.getgeoapi.com/v2/currency/convert?api_key=fc85a4ef6482be22cddea507921311bc4a8afccb&from=USD&to=NGN&amount=1&format=json`) {
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
        const theRate = responseData.rates.NGN.rate;
        const rateOffSet = 327.75;
        const theRateInIntergers = parseFloat(theRate)
        const actualAmount = rateOffSet + theRateInIntergers
        console.log(responseData.rates.NGN.rate); // Display the response data
        display.innerHTML = actualAmount;
        return responseData.rates.NGN.rate;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}

// Example usage: Retrieve data from an API endpoint
// const API_KEY = "fc85a4ef6482be22cddea507921311bc4a8afccb";
// const apiUrl = `https://api.getgeoapi.com/v2/currency/convert
// ?${API_KEY}
// &from=NGN
// &to=USD
// &amount=1
// &format=json`; // Replace with your API endpoint
