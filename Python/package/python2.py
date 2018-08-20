import os
annee = input("Entrez ici votre année de naissance")
try:
    annee = int(annee)
except ValueError:
    print("la valeur n'a pas été définie veuillez en définir une")
except TypeError:
    print("Vous ne pouvez entrer que des nombres entiers")
os.system("pause")
