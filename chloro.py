import os
import folium
import pandas as pd
import csv

# how-to here (https://python-graph-gallery.com/292-choropleth-map-with-folium/)
geo_arrond = os.path.join('lyon_arron.json')


donnees = os.path.join('../full.csv')
donnees = pd.read_csv('../full.csv')

# Initialize the map:
m = folium.Map(location=[45.750000, 4.850000], zoom_start=13)
 
# Add the color for the chloropleth:
m.choropleth(
 geo_data=geo_arrond,
 name='choropleth',
 data=donnees,
 columns=['latitude', 'longitude'],
 key_on='feature.id',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='valeurs foncieres'
)
folium.LayerControl().add_to(m)
 
# Save to html
m.save('test.html')

 