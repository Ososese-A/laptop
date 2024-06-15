const url = 'https://google-translate1.p.rapidapi.com/language/translate/v2/detect';

const word = document.getElementById("word");
const translated = document.querySelector(".translated");
const btn = document.getElementById("btn");

const fetcher = async (options) => {
    try {
        const response = await fetch(url, options);
        const rest = await response.json();
        const result = rest.data.detections[0][0].language;
        console.log(result);
        console.log(rest)
        translated.innerHTML = result;
    } catch (error) {
        console.error(error);
    }
}


btn.onclick = async () => {
   const res =  word.value;

   const options = {
	method: 'POST',
	headers: {
		'content-type': 'application/x-www-form-urlencoded',
		'Accept-Encoding': 'application/gzip',
		'X-RapidAPI-Key': '5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580',
		'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
	},
	body: new URLSearchParams({
		q: res
	})
};

fetcher (options);
}
