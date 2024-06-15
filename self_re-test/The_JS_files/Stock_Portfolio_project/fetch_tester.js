const dis = document.getElementById("display");
const display = document.getElementById("rateDisplay");
const disp = document.getElementById("nairaDisplay");
const out_one = document.getElementById("one");
const out_two = document.getElementById("two");
const out_three = document.getElementById("three");
const out_four = document.getElementById("four");
const out_five = document.getElementById("five");
const out_six = document.getElementById("six");
const MSFT = "https://realstonks.p.rapidapi.com/MSFT"; 
const getMsft = async (url = MSFT) => {
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
        window.realStockPrice = parseFloat(stockPrice);
        console.log(responseData.price); 
        out_one.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}


const NFLX = "https://realstonks.p.rapidapi.com/NFLX";
const getNflx = async (url = NFLX) => {
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
        window.realStockPrice = parseFloat(stockPrice);
        console.log(responseData.price); 
        out_two.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}


const APPL = "https://realstonks.p.rapidapi.com/APPL";
const getAppl = async (url = APPL) => {
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
        window.realStockPrice = parseFloat(stockPrice);
        console.log(responseData.price); 
        out_three.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}



const TSLA = "https://realstonks.p.rapidapi.com/TSLA";
const getTsla = async (url = TSLA) => {
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
        window.realStockPrice = parseFloat(stockPrice);
        console.log(responseData.price); 
        out_four.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}



const WBD = "https://realstonks.p.rapidapi.com/WBD";
const getWbd = async (url = WBD) => {
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
        window.realStockPrice = parseFloat(stockPrice);
        console.log(responseData.price); 
        out_five.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}



const PARA = "https://realstonks.p.rapidapi.com/PARA";
const getPara = async (url = PARA) => {
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
        window.realStockPrice = parseFloat(stockPrice);
        console.log(responseData.price); 
        out_six.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}




const DIS = "https://realstonks.p.rapidapi.com/DIS";
const JAKK = "https://realstonks.p.rapidapi.com/JAKK";
const HAS = "https://realstonks.p.rapidapi.com/HAS";
const SONY = "https://realstonks.p.rapidapi.com/SONY";
const AMZN = "https://realstonks.p.rapidapi.com/AMZN";
const EBAY = "https://realstonks.p.rapidapi.com/EBAY";
const COKE = "https://realstonks.p.rapidapi.com/COKE";
const DPZ = "https://realstonks.p.rapidapi.com/DPZ";
const U = "https://realstonks.p.rapidapi.com/U";
const NKE = "https://realstonks.p.rapidapi.com/NKE";
const V = "https://realstonks.p.rapidapi.com/V";
const META = "https://realstonks.p.rapidapi.com/META";
const DELL = "https://realstonks.p.rapidapi.com/DELL";
const UA = "https://realstonks.p.rapidapi.com/UA";
const MNST = "https://realstonks.p.rapidapi.com/MNST";
const HPE = "https://realstonks.p.rapidapi.com/HPE";
const MDLZ = "https://realstonks.p.rapidapi.com/MDLZ";
const MAT = "https://realstonks.p.rapidapi.com/MAT";
const TGT = "https://realstonks.p.rapidapi.com/TGT";
const WMT = "https://realstonks.p.rapidapi.com/WMT";
const GOOGL = "https://realstonks.p.rapidapi.com/GOOGL";
const PAYC = "https://realstonks.p.rapidapi.com/PAYC";
const PYPL = "https://realstonks.p.rapidapi.com/PYPL";
const ADBE = "https://realstonks.p.rapidapi.com/ADBE";
const NVDA = "https://realstonks.p.rapidapi.com/NVDA";
const INTC = "https://realstonks.p.rapidapi.com/INTC";
const DBX = "https://realstonks.p.rapidapi.com/DBX";
const WKHS = "https://realstonks.p.rapidapi.com/WKHS";
const CROX = "https://realstonks.p.rapidapi.com/CROX";
const LULU = "https://realstonks.p.rapidapi.com/LULU";
const SKX = "https://realstonks.p.rapidapi.com/SKX";
const VSAT = "https://realstonks.p.rapidapi.com/VSAT";
const WEN = "https://realstonks.p.rapidapi.com/WEN";
const MCD = "https://realstonks.p.rapidapi.com/MCD";
const HSY = "https://realstonks.p.rapidapi.com/HSY";
const K = "https://realstonks.p.rapidapi.com/K";


const getStockPrice = async (url = "") => {
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
        // const stockPrice = responseData.price;
        // window.realStockPrice = parseFloat(stockPrice);
        // console.log(responseData.price); 
        // dis.innerHTML = stockPrice;
        return responseData.price;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}




const get_Ngn_Usd_Rate = async (url = `https://api.getgeoapi.com/v2/currency/convert?api_key=fc85a4ef6482be22cddea507921311bc4a8afccb&from=USD&to=NGN&amount=1&format=json`) => {
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
        console.log(responseData.rates.NGN.rate); // Display the response data
        display.innerHTML = actualAmount;
        return responseData.rates.NGN.rate;
    } catch (error) {
        console.error("Error while fetching:", error);
    }
}

const converted = () => {
    naira = realStockPrice * actualAmount;
    disp.innerHTML = naira;
}