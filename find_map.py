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

    def draw_arrondissement(self, geo, couleur):
        folium.Choropleth(
            geo_data=geo,
            name='choropleth',
            columns=['latitude', 'longitude'],
            key_on='feature.id',
            fill_color=couleur,
            fill_opacity=0.3,
            line_opacity=0.2,
            legend_name='valeurs foncieres'
        ).add_to(self.map)

    def sauvegarde(self):
        # Save to html
        folium.LayerControl().add_to(self.map)
        self.map.save('test.html')
