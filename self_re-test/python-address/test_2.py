import geocoder
import folium

g = geocoder.ip("me")
# g = geocoder.ip("146.78.3.8")

my_add = g.latlng

my_map1 = folium.Map(
    location=my_add,
    zoom_start=12)

#to add the circle marker 
folium.CircleMarker(location=my_add,
                    radius=50, popup="Hamitkoy").add_to(my_map1)

folium.Marker(my_add, popup="Hamitkoy").add_to(my_map1)

my_map1.save("my_map.html")