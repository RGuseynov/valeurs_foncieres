import os
import folium
import pandas as pd
import csv

# how-to here (https://python-graph-gallery.com/292-choropleth-map-with-folium/)
#geo_arrond = os.path.join('lyon_arron.json')
geo_arron = "https://transcode.geo.data.gouv.fr/services/5bfd5598cb932f8781e55ede/feature-types/ms:adr_voie_lieu.adrarrond?format=GeoJSON&projection=WGS84"


# Initialize the map:
m = folium.Map(location=[45.750000, 4.850000], zoom_start=12)
 
folium.GeoJson(
    geo_arron,
    name='geojson'
).add_to(m)

# text = 'your text here'
# iframe = folium.IFrame(text, width=700, height=450)
# popup = folium.Popup(iframe, max_width=3000)
# Text = folium.Marker(location=[45.750000,4.850000], popup=popup,
#                      icon=folium.Icon(icon_color='green'))
# m.add_child(Text)

# Add the color for the chloropleth:
m.choropleth(
    geo_data=geo_arron,
    name='choropleth',
    columns=['latitude', 'longitude'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.3,
    line_opacity=0.2,
    legend_name='valeurs foncieres',
)


folium.LayerControl().add_to(m)

# Save to html
m.save('test.html')


