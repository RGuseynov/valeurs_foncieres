import pandas as pd
import numpy as np
from find_map import Map
import matplotlib.pyplot as plt
import json


geo_arron = "https://transcode.geo.data.gouv.fr/services/5bfd5598cb932f8781e55ede/feature-types/ms:adr_voie_lieu.adrarrond?format=GeoJSON&projection=WGS84"


def trie_df(df):
    df = df[["date_mutation", "valeur_fonciere", "type_local", "surface_reelle_bati", "code_postal"]]
    df = df[df["type_local"] == "Appartement"]
    df = df[(df['code_postal'] > 69000) & (df['code_postal'] < 69010)]
    df = df[(df["valeur_fonciere"] < 1500000) & (df["valeur_fonciere"] > 50000)]
    df = df[(df["surface_reelle_bati"] > 8) & (df["surface_reelle_bati"] < 220)]
    return df


def prix_m2(df):
    return df["valeur_fonciere"] / df["surface_reelle_bati"]  # renvoi une pandas Serie


def prix_moyen_arr(df):
    list_prix_moy_arr = []
    for i in range(69001, 69010):
        list_prix_moy_arr.append(prix_m2(df[df["code_postal"] == i]).mean())
    return list_prix_moy_arr  # renvoi une list des prix moyens: un indice = un arrondissement

def add_layers(self, geo_arron)
        folium.GeoJson(
            geo_arron, 
            name='geojson'
        ).add_to(self.map)

def couleur_selon_variation(value):
    if value > 1.05:
        return "green"
    elif value < 0.95:
        return "red"
    else:
        return "yellow"

# création d'une liste(année) de listes(prix moyen) a partir des 5 fichiers csv
# list_prix_arr = []
# for i in range(2014, 2019):
#     list_prix_arr.append(prix_moyen_arr(trie_df(pd.read_csv("data_foncieres_en_csv/" + str(i) + ".csv"))))

# resultat du traitement des 5 csv pour aller plus vite
list_prix_arr = [[4964.262141756308, 5074.058832737507, 5697.894768056259, 4080.390297296636, 3845.1724661864178, 4744.28148010927, 3811.542349202425, 4582.990352101632, 4644.173093028567], [4698.364896924889, 4805.461847638455, 4624.67924498137, 4157.76416235475, 4009.4547640682267, 4671.374951935903, 4658.873258924146, 3682.76829757539, 3696.1638039613745], [5272.997350506025, 4713.039823956925, 4221.793748448441, 5339.114930044605, 4163.083236880928, 4663.325763362831, 4645.9633991358605, 4403.069862308347, 3690.1486070219266], [5584.138402553896, 4761.21438427903, 4785.793453593581, 5823.503135377577, 4913.829403061922, 5600.738272074323, 5220.065902202487, 4931.916080221787, 4544.0622240080575], [5119.320707961439, 5893.178359912912, 5555.614097261336, 6158.500750125721, 3252.175505739831, 5821.289326220377, 4202.091627441864, 4289.83807231761, 3229.389638734088]]

# creation d'un dataframe a partir de la list de listset et inversion index/column avec transpose
df_prix = pd.DataFrame(list_prix_arr, index=[i for i in range(2014, 2019)], columns=[i for i in range(1, 10)])
df_prix = df_prix.transpose()

# creation d'une copie du dataframe
df_variation = df_prix.copy()

# calcul de la variation et effacement de l'annee 2014
for i in range(2015, 2019):
    df_variation[i] = df_prix[i] / df_prix[i - 1]
del df_variation[2014]

variation_2014_2018 = pd.DataFrame(df_prix[2018] / df_prix[2014], columns=['Variation'])
variation_2014_2018["Couleur"] = variation_2014_2018["Variation"].map(lambda x: couleur_selon_variation(x))

print(variation_2014_2018)

# visualisation sur plt
# data_trie.plot(kind='scatter', x='surface_reelle_bati', y='valeur_fonciere', color='red')
# plt.show()

map_Lyon = Map(45.763664999057148, 4.856268)

with open("adr_voie_lieu.json", "r") as file:
    json_arr = json.load(file)

for arr in json_arr["features"]:
    geodata = {"type": "FeatureCollection", "features": [arr]}
    print(geodata)
    print(arr["properties"]["gid"])
    print(variation_2014_2018.loc[int(arr["properties"]["gid"]), ["Couleur"]].values[0])
    map_Lyon.draw_arrondissement(geodata, variation_2014_2018.loc[int(arr["properties"]["gid"]), ["Couleur"]].values[0])

map_Lyon.sauvegarde()