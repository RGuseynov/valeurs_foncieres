import folium


class Map:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
        self.map = folium.Map(
            location=[longitude, latitude],
            tiles='openstreetmap',
            zoom_start=13,
            attr='My Data Attribution'
        )

    def draw_map(self, iter_longitude, iter_latitude):
        for i in range(len(iter_longitude)):
            folium.Marker(
                location=[iter_longitude[i], iter_latitude[i]],
                icon=folium.Icon(color='white', icon='info-sign')
            ).add_to(self.map)
        self.map.save('index.html')


list_longitude = [45.750000, 45.7529002, 45.7603831, 45.774195, 45.762,45.7614853, 45.7460481, 45.7348248, 45.7739471]
list_latitude = [4.8300276, 4.8268543, 4.849664, 4.827882, 4.827, 4.843362, 4.8417503, 4.8741702, 4.8069094]

map1 = Map(list_longitude[0], list_latitude[0])

map1.draw_map(list_longitude, list_latitude)