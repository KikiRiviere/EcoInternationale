from src.fonctions import fonction_select,possibilites


# Exatement le même fonctionnement que dans 2_statistiques_aop.py (mais avec seulement 2 fonctions disponibles au choix)
print("----\nBienvenue dans l'exploreur d'option !\n----")


possibilites()
choix_fonction = int(input("Choississez une fonction à mettre en avant : "))
fonction_select[choix_fonction-1]()
while True :
    print("\n----\nVoulez-vous voir une autre fonction ? (Oui/Non)\n----")
    yes = input("> ")
    if yes == "Oui" or yes == "oui" or yes == "OUI":
        possibilites()
        choix_fonction = int(input("Choississez une fonction à mettre en avant : "))
        fonction_select[choix_fonction-1]()
    elif yes == "NON" or yes == "Non" or yes == "non" :
        print("\n----\nAu revoir !\n----")
        break
    else :
        print("\n----\nErreur de saisie !\n----")
