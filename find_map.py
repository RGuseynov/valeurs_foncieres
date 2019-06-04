import folium
import vincent

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

    # def draw_map(self, iter_longitude, iter_latitude):
    #     for i in range(len(iter_longitude)):
    #         folium.Marker(
    #             location=[iter_longitude[i], iter_latitude[i]],
    #             icon=folium.Icon(color='white', icon='info-sign')
    #         ).add_to(self.map)
    #     self.map.save('test.html')


    def draw_arrondissement(self, geo, couleur):
        folium.Choropleth(
            geo_data=geo,
            name='choropleth',
            columns=['latitude', 'longitude'],
            key_on='feature.id',
            fill_color=couleur,
            fill_opacity=0.3,
            line_opacity=1,
            line_weight=1,
            line_color='blue',
            legend_name='valeurs foncieres'
        ).add_to(self.map)
        # folium.LayerControl().add_to(self.map)

    def sauvegarde(self):
        # Save to html
        folium.LayerControl().add_to(self.map)
        self.map.save('test.html')

    def add_marker(self, serie, longitude, latitude, arrondissement):
        liste_annee = []
        liste_valeur = []
        for annee in serie.index :
            liste_annee.append(annee)
        for valeur in serie.values :
            liste_valeur.append(valeur)

        scatter_points = {
            'x': liste_annee,
            'prix au m2': liste_valeur,
        }

        scatter_chart = vincent.Bar(scatter_points,
                                iter_idx='x',
                                width=300,
                                height=200)
        scatter_chart.axis_titles(x='Année', y='Prix au m2')
        scatter_chart.legend(title=arrondissement)

        popup = folium.Popup()
        folium.Vega(scatter_chart, width = 400, height=250).add_to(popup)
        folium.Marker([longitude, latitude], popup=popup).add_to(self.map)
