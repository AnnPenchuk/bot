import requests


url = "https://numbersapi.p.rapidapi.com/1729/math"

querystring = {"fragment":"true","json":"true"}

headers = {
	"X-RapidAPI-Key": "ac4c7b15c4mshf42df525a11de30p17f456jsnadcab34e3b42",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)