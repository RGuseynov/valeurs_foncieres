import csv
import pandas as pd
import folium

data = pd.read_csv('data_game.csv')


df1 = data[['valeur_fonciere', 'longitude','latitude']]

df1 = df1.loc[(df1['valeur_fonciere'] == 19550000) ,:]
df1 = df1.dropna()

locations = df1[['latitude', 'longitude']]
locationlist = locations.values.tolist()


map = folium.Map(location=[45.372, 4.8614], zoom_start=12)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup='point').add_to(map)
map.save('carte3.html')