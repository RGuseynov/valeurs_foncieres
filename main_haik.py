import folium


m = folium.Map(location=[45.750000, 4.850000])




# type de carte
folium.Map(
    location=[45.750000, 4.850000],
    tiles='openstreetmap',
    zoom_start=13,
    attr='My Data Attribution'
)

tooltip = 'Click me!' #nom de la ville


# les markeurs pour les lieux selectionnés
# folium.Marker([45.750000, 4.850000], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(m)


folium.Marker(
    location=[45.7333, 4.9167],
    popup='Some Other Location',
    tooltip=tooltip,
    icon=folium.Icon(color='pink', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.7667, 4.8833],
    popup='Some Other Location',
    icon=folium.Icon(color='purple', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[48.856614, 2.3522219],
    popup='Some Other Location',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[5.447427, 43.529742],
    popup='Some Other Location',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)


# lat et long lorsque l'util clique sur la carte
# m.add_child(folium.LatLngPopup())


m.save('index.html')