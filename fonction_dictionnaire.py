def recuperation_ligne1(fichier_text):
    with open(fichier_text, "r") as file:
        ligne1 = file.readline().strip()
    return ligne1


def creation_dictionnaire(text_colonnes):
    list_colonnes = text_colonnes.split(",")
    dictionnaire = {}
    for elem in list_colonnes:
        dictionnaire[elem] = []
    return dictionnaire


def remplissage_dictionnaire(fichier_text):
    dictionnaire = creation_dictionnaire(recuperation_ligne1(fichier_text))
    with open(fichier_text, "r") as file:
        file.readline()
        lines = file.readlines(1000)
        for line in lines:
            list_contenu_ligne = line.strip().split(",")
            i = 0
            for k, v in dictionnaire.items():
                v.append(list_contenu_ligne[i])
                i += 1
    return dictionnaire


def effacement_cles(dictionnaire, *keys):
    for key in keys:
        dictionnaire.pop(key, None)


def selection_cles(dictionnaire, *keys):
    nouveau_dictionnaire = {key: dictionnaire[key] for key in keys}
    return nouveau_dictionnaire