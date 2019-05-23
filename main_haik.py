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
    location=[45.7694158, 4.8300276],
    popup='Mairie 1e',
    icon=folium.Icon(color='white', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.7529002, 4.8268543],
    popup='Mairie 2e',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.7603831, 4.849664],
    popup='Mairie 3e',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.774195, 4.827882],
    popup='Mairie 4e',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.762, 4.827],
    popup='Mairie 5e',
    tooltip=tooltip,
    icon=folium.Icon(color='pink', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.7614853, 4.843362],
    popup='Mairie 6e',
    icon=folium.Icon(color='purple', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.7460481, 4.8417503],
    popup='Mairie 7e',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.7348248, 4.8741702],
    popup='Mairie 8e',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)

folium.Marker(
    location=[45.7739471, 4.8069094],
    popup='Mairie 9e',
    icon=folium.Icon(color='lightblue', icon='info-sign')
).add_to(m)


# lat et long lorsque l'util clique sur la carte
# m.add_child(folium.LatLngPopup())


m.save('index.html')