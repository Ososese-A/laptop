import phonenumbers
import opencage
import folium
from phonenumbers import geocoder




number = "+2348134266823"


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

api_key = "fd3fb55f5aaf49aba2519c3f8bf74273"

geocoder = OpenCageGeocode(api_key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)


myMap = folium.Map(location=[lat,lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocationsema.html")