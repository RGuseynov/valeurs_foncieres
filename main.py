import pandas as pd
import numpy as np
from find_map import Map
import matplotlib.pyplot as plt


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
list_prix_arr = []
for i in range(2014, 2019):
    list_prix_arr.append(prix_moyen_arr(trie_df(pd.read_csv("data_foncieres_en_csv/" + str(i) + ".csv"))))

# creation d'un dataframe a partir de la list de listset et inversion index/column avec transpose
df_prix = pd.DataFrame(list_prix_arr, index=[i for i in range(2014, 2019)], columns=[i for i in range(1, 10)])
df_prix = df_prix.transpose()

# creation d'une copie du dataframe
df_variation = df_prix.copy()

# calcul de la variation et effacement de l'annee 2014
for i in range(2015, 2019):
    df_variation[i] = df_prix[i] / df_prix[i - 1]

del df_variation[2014]

print(df_variation)


# visualisation sur plt
# data_trie.plot(kind='scatter', x='surface_reelle_bati', y='valeur_fonciere', color='red')
# plt.show()


# df = pd.DataFrame(dict_traite)

# df_appartement = df.loc[df["type_local"] == "Appartement"]

# df_appartement_lyon = df_appartement.loc[df_appartement['code_postal'].str.startswith("6900")]
# print(df_appartement_lyon)


# list_longitude = [45.750000, 45.7529002, 45.7603831, 45.774195, 45.762,45.7614853, 45.7460481, 45.7348248, 45.7739471]
# list_latitude = [4.8300276, 4.8268543, 4.849664, 4.827882, 4.827, 4.843362, 4.8417503, 4.8741702, 4.8069094]

# map1 = Map(list_longitude[0], list_latitude[0])

# map1.draw_map(list_longitude, list_latitude)

