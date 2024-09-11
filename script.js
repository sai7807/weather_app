
const options = {
	method: 'GET',
	Headers: {
		'x-rapidapi-key': 'oRqniHlrCRxtE4FBMlCrKA==TpKkNKuuzcrswUs6',
		'x-rapidapi-host': 'weather-by-api-ninjas.p.rapidapi.com'
	}
};

const getWeather = (city)=>{
	cityName.innerHTML = city
fetch('https://api.api-ninjas.com/v1/weather?city=' + city, options)
	.then(Response => Response.json())
	.then(Response => {

		console.log(Response)



		cloud_pct.innerHTML = Response.cloud_pct
		feels_like.innerHTML = Response.feels_like
		humidity.innerHTML = Response.humidity
		humidity2.innerHTML = Response.humidity
		max_temp.innerHTML = Response.max_temp
		min_temp.innerHTML = Response.min_temp
		sunrise.innerHTML = Response.sunrise
		sunset.innerHTML = Response.sunset
		temp.innerHTML = Response.temp
		temp2.innerHTML = Response.temp
		wind_degrees.innerHTML = Response.wind_degrees
		wind_speed.innerHTML = Response.wind_speed
		wind_speed2.innerHTML = Response.wind_speed


	})
	.catch(err => console.error(err));
}

Submit.addEventListener("click", (e)=>{
	e.preventDefault()
	getWeather(city.value)

})

