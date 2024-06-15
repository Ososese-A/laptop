const for_usd_a = document.getElementById("msft_mon_usd_a");
const for_usd_b = document.getElementById("msft_mon_usd_b");
const for_naira_a = document.getElementById("msft_mon_ngn_a");
const for_naira_b = document.getElementById("msft_mon_ngn_b");
const for_time_a = document.getElementById("msft_mon_time_a");
const for_time_b = document.getElementById("msft_mon_time_b");
const for_time_avg = document.getElementById("msft_mon_time_avg");
const avg_ngn = document.getElementById("msft_mon_ngn_avg");
const avg_usd = document.getElementById("msft_mon_usd_avg");
const MSFT = "https://realstonks.p.rapidapi.com/MSFT"; 


const fetchData = async (url= MSFT) => {
    try {
        const options = {
            method: 'GET',
            headers: {
                'X-RapidAPI-Key': '5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580',
                'X-RapidAPI-Host': 'realstonks.p.rapidapi.com'
            }
        };
        const response = await fetch(url, options);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const responseData = await response.json(); 
        const stockPrice = responseData.price;
        window.realStockPrice1 = parseFloat(stockPrice);
        console.log(responseData); 
        // out_one.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}


const formatNumberWithCommas = (number) => {
    const parts = number.toFixed(3).split('.');
    const integerPart = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return `${integerPart}.${parts[1]}`;
}


const convertToNairaA = async () => {
    await get_Ngn_Usd_Rate(`https://api.getgeoapi.com/v2/currency/convert?api_key=fc85a4ef6482be22cddea507921311bc4a8afccb&from=USD&to=NGN&amount=1&format=json`);
    naira = realStockPrice1 * actualAmount;
    window.approx1 = parseFloat(naira)
    for_naira_a.innerHTML = formatNumberWithCommas(approx1);
}


const convertToNairaB = async () => {
    await get_Ngn_Usd_Rate(`https://api.getgeoapi.com/v2/currency/convert?api_key=fc85a4ef6482be22cddea507921311bc4a8afccb&from=USD&to=NGN&amount=1&format=json`);
    naira = realStockPrice1 * actualAmount;
    window.approx2 = parseFloat(naira)
    for_naira_b.innerHTML = formatNumberWithCommas(approx2);
}


const get_Ngn_Usd_Rate = async (url) => {
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
        window.actualAmount = rateOffSet + theRateInIntergers
        // console.log(responseData.rates.NGN.rate); // Display the response data
        // display.innerHTML = actualAmount;
        return responseData.rates.NGN.rate;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}


const getDateAndTimeAvg = (date = new Date()) => {
    const options = {
        hour: 'numeric',
        minute: '2-digit',
        month: 'long',
        day: 'numeric',
        year: 'numeric',
        hour12: true
    };

    const msftMonDateAvg = new Intl.DateTimeFormat('en-US', options).format(date);
    // console.log(msftMonDateAvg);
    for_time_avg.innerHTML = msftMonDateAvg;

    // Save the formatted date and time to local storage
    localStorage.setItem('msftMonDateAvg', msftMonDateAvg);
}


const getDateAndTimeA = (date = new Date()) => {
    const options = {
        hour: 'numeric',
        minute: '2-digit',
        month: 'long',
        day: 'numeric',
        year: 'numeric',
        hour12: true
    };

    const msftMonDateA = new Intl.DateTimeFormat('en-US', options).format(date);
    // console.log(msftMonDateA);
    for_time_a.innerHTML = msftMonDateA;

    // Save the formatted date and time to local storage
    localStorage.setItem('msftMonDateA', msftMonDateA);
}


const getDateAndTimeB = (date = new Date()) => {
    const options = {
        hour: 'numeric',
        minute: '2-digit',
        month: 'long',
        day: 'numeric',
        year: 'numeric',
        hour12: true
    };

    const msftMonDateB = new Intl.DateTimeFormat('en-US', options).format(date);
    // console.log(msftMonDateB);
    for_time_b.innerHTML = msftMonDateB;

    // Save the formatted date and time to local storage
    localStorage.setItem('msftMonDateB', msftMonDateB);
}


const avgNgn = async (approx2 = 0) => {
    ngnAvg = await formatNumberWithCommas(((approx1 + approx2) / 2));
    avg_ngn.innerHTML = ngnAvg;
}


const avgUsd = async (realStockPrice2 = 0) => {
    usdAvg = await formatNumberWithCommas(((realStockPrice2 + realStockPrice1) / 2));
    avg_usd.innerHTML = usdAvg;
}


const printerForA = async () => {
    await fetchData()
    for_usd_a.innerHTML = formatNumberWithCommas(realStockPrice1);
    await convertToNairaA()
    getDateAndTimeA()
    getDateAndTimeAvg()
    avgNgn()
    avgUsd()
}


const printerForB = async () => {
    await fetchData()
    const realStockPrice2 = realStockPrice1;
    for_usd_b.innerHTML = formatNumberWithCommas(realStockPrice2);
    await convertToNairaB()
    getDateAndTimeB()
    getDateAndTimeAvg()
    avgNgn(approx2)
    avgUsd(realStockPrice2)
}


const getMsft = (set) => {
    if (set == 'a') {
        // alert("It is working")
        printerForA();
    }
    if (set == 'b') {
        // alert("It is not working")
        printerForB();
    }
}

// 1. the next thing now is to add the 6 hours restriction feature then the local storage features 
// 2. after that add a refetch condition where if the stuff are already in local storage you decide 
//    if you want to overide or cancle with the dialogue pop up
// 3. after that work out how to set it all up for days of the week 
// 4. then plan out how to do it all for months and then years 
// 5. then add a feature to check if it's taking too much local storage space so you can now use a txt file to store old data 