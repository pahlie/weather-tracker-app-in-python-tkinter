import folium

# create a map centered on a specific latitude and longitude
m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# display the map
m.save('map.html')
