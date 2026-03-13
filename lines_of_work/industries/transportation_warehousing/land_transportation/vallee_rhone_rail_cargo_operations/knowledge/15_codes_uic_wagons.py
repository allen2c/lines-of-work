"""Knowledge item: codes UIC wagons."""

title = "Codes UIC et Identification des Wagons"

content = """
Les codes UIC permettent d'identifier precisement le type, la charge utile, et
les equipements d'un wagon. Chaque wagon porte des plaques et marquages
reglementaires.

**Structure du numero wagon:** 12 chiffres : 2 pour le pays, 2 pour le
proprietaire, 7 pour le numero, 1 pour la cle de controle. Des lettres
supplementaires indiquent le type (e, f, s, etc.) et les caracteristiques
( chauffage, frein, etc.).

**Usage operationnel:** Lors de la planification d'un convoi, la compatibilite
wagons/marchandises et wagons/locomotive doit etre verifiee. Un wagon
inadapté (ex. pas de frein continu pour un train longue distance) ne peut pas
circuler. Les fiches techniques wagons sont consultees systematiquement.
"""  # noqa: E501

version = "0.0.1"
