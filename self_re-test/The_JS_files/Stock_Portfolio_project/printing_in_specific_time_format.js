function formatDateTime(date) {
    const options = {
        hour: 'numeric',
        minute: '2-digit',
        month: 'long',
        day: 'numeric',
        year: 'numeric',
        hour12: true
    };

    const formattedDateTime = new Intl.DateTimeFormat('en-US', options).format(date);
    console.log(formattedDateTime);

    // Save the formatted date and time to local storage
    localStorage.setItem('myFormattedDateTime', formattedDateTime);
}

// Example usage:
const currentDate = new Date();
formatDateTime(currentDate); // Output: "12:30 PM 24 April 2023"

// Retrieve the saved date and time from local storage
const savedDateTime = localStorage.getItem('myFormattedDateTime');
console.log('Saved date and time:', savedDateTime);