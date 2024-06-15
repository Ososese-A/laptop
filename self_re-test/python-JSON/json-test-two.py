import json
import requests

url = "https//api.punkapi.com/v2/beers?food=burger"

s = requests.get(url)

data = json.loads(s.text)



beer_list = []

for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']

    beer_item = {
        "name" : name,
        "tagline" : tagline,
        "abv" : abv}
    beer_list.append(beer_item)

print(beer_list)
