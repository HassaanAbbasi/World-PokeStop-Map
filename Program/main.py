import folium
import pandas

data = pandas.read_csv("PokeGoLocations.csv")

#Initializing the map to start at Toronto
map = folium.Map(location = [43.6532, -79.3832], zoom_start = 12, min_zoom = 3)

#This object holds all the locations
stops = folium.FeatureGroup(name = "Pokestops")

#Adding places to "stops"
for lat, lon, name in zip(data["Latitude"], data["Longitude"], data["Location Name"]):
    stops.add_child(folium.Marker(location = [lat,lon], popup = f"{name}", icon = folium.Icon(color = "cadetblue")))
    
map.add_child(stops)

map.save("PokeStops.html")