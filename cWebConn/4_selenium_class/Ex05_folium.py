# Ex05_folium.py

import folium

map_osm = folium.Map(location=[37.572463, 126.975611], zoom_start=17)
folium.Marker(location=[37.572463, 126.975611],
              popup="세종문화회관",
              icon=folium.Icon(color="red", icon="info-sign")).add_to(map_osm)
folium.CircleMarker(location=[37.572463, 126.975611], popup="광화문역", radius=100, color="red", fill_color="#AAAA33").add_to(map_osm)
map_osm.save("./map/map4.html")