function printHelloWorld() {
    const now = new Date();
    const currentHour = now.getHours();

    if (currentHour === 7) {
        console.log("Hello");
    } else if (currentHour === 13) { // 7 AM + 6 hours
        console.log("World");
    }
}