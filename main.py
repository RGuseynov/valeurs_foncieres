import pandas as pd
import numpy as np
from find_map import Map
import matplotlib.pyplot as plt
import json


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


# création d'une liste(année) de listes(prix moyen) a partir des 5 fichiers csv
# list_prix_arr = []
# for i in range(2014, 2019):
#     list_prix_arr.append(prix_moyen_arr(trie_df(pd.read_csv("data_foncieres_en_csv/" + str(i) + ".csv"))))

# creation d'un dataframe a partir de la list de listset et inversion index/column avec transpose
# df_prix = pd.DataFrame(list_prix_arr, index=[i for i in range(2014, 2019)], columns=[i for i in range(1, 10)])
# df_prix = df_prix.transpose()

# creation d'une copie du dataframe
# df_variation = df_prix.copy()
#
# # calcul de la variation et effacement de l'annee 2014
# for i in range(2015, 2019):
#     df_variation[i] = df_prix[i] / df_prix[i - 1]
# del df_variation[2014]
#
# print(df_variation)

# visualisation sur plt
# data_trie.plot(kind='scatter', x='surface_reelle_bati', y='valeur_fonciere', color='red')
# plt.show()

with open("adr_voie_lieu.json", "r") as file:
    json_arr = json.load(file)


for arr in json_arr["features"]:
    geodata = {"type": "FeatureCollection", "features": [arr]}