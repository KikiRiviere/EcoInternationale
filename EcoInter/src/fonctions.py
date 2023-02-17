def possibilites():
    choix_list = ["Calculer le taux de change réel bilatérale.","Calculer le taux de change réel bilatérale inversé.","Change fixe - Comment maintenir la parité de sa monnaie?","Appréciation ou dépréciation par rapport au taux d'inflation?","Choix du titre financier par rapport au taux de change entre deux pays.",
                  "Calculer le taux de change effectif en fonction de X pays.","Voir si une monnaie est sous ou sur-évaluée grâce au taux de change PPA."]
    for i in range(0,len(choix_list)):
        print(str(i+1)," - ",str(choix_list[i]))

def tx_change_bilaterale_reel(): 
    print("\n\n----\nVous entrez dans l'option 1 !\n => Calculer le taux de change réel bilatérale\n----")
    montant = float(input('Veuillez entrer le montant du produit dans la monnaie d\'origine : '))
    
    base_mon = str(input('Veuillez entrer la monnaie d\'origine du produit : '))
    arriv_mon = str(input('Veuillez entrer la monnaie visée du produit pour faire le taux de change : '))
    
    montant_mon = float(input('Veuillez entrer le montant du taux de change (ex: 1.02894) : '))
    
    final = montant*montant_mon
    print("Pour un produit qui vaut " + str(montant) + " " + str(base_mon) + ", ce produit vaut " + str(final) + " " + str(arriv_mon) + ".")
    if montant_mon > 1 :
        print("Il faut noter que la monnaie " + str(arriv_mon) + " est moins forte que la monnaie " + str(base_mon)+ ".")
    else :
        print("Il faut noter que la monnaie " + str(arriv_mon) + " est plus forte que la monnaie " + str(base_mon)+ ".")
    
def tx_change_bilaterale_reel_inverse(): 
    print("\n\n----\nVous entrez dans l'option 2 !\n => Calculer le taux de change réel bilatérale inversé.\n----\n")
    base_mon = str(input('Veuillez entrer la monnaie d\'origine du produit : '))
    
    arriv_mon = str(input('Veuillez entrer la monnaie visée du produit pour faire le taux de change : '))
    montant_mon = float(input('Veuillez entrer le montant du taux de change (ex: 1.02894) : '))
    
    montant = float(input('Veuillez entrer le montant du produit dans la monnaie visée : '))
    
    final = montant/montant_mon
    print("Pour un produit qui vaut " + str(montant) + " " + str(base_mon) + ", ce produit vaut " + str(final) + " " + str(arriv_mon) + ".")
    if montant_mon < 1 :
        print("Il faut noter que la monnaie " + str(base_mon) + " est moins forte que la monnaie " + str(arriv_mon)+ ".")
    else :
        print("Il faut noter que la monnaie " + str(base_mon) + " est plus forte que la monnaie " + str(arriv_mon)+ ".")

def change_fixe(): 
    print("\n\n----\nVous entrez dans l'option 3 !\n => Change fixe - Comment maintenir la parité de sa monnaie?\n----")
    parite_officielle = float(input("Entrez la parité officielle du taux de change (ex : 1$ = 6MIN (Notez 6) ) : "))
    marge = float(input("Entrez la marge de fluctuation (en %) : "))
    tx_TC = float(input("Entrez le taux de change sur le marché (ex : 1$ = 6MIN (Notez 6)) : "))
    resultatA = parite_officielle * (1-marge/100)
    resultatB = parite_officielle * (1+marge/100)
    if tx_TC < resultatA :
        print("----\nLe taux de change sur le marché doit augmenter donc la monnaie doit se déprécier !\n----")
    elif resultatA < tx_TC < resultatB :
        print("----\nLe taux de change sur le marché est dans la marge de fluctuation, il n'y a rien besoin de faire !\n----")
    else :
        print("----\nLe taux de change sur le marché doit baisser donc la monnaie doit s'apprécier !\n----")

def tx_inflation_tx_change():
    print("\n\n----\nVous entrez dans l'option 4 !\n => Appréciation ou dépréciation par rapport au taux d'inflation?\n----\n")
    tx_infla1 = float(input("Indiquez le taux d'inflation du pays de départ (en pourcentage) : "))
    tx_infla2 = float(input("Indiquez le taux d'inflation du pays d'arrivée (en pourcentage) : "))
    if tx_infla1 > tx_infla2 :
        tx_final = tx_infla1 - tx_infla2
        print("Selon la théorie de la PPA relative, la monnaie de départ s'est dépréciée de " + str(tx_final) + "% par rapport à la monnaie d'arrivée !")
    elif tx_infla2 > tx_infla1 :
        tx_final = tx_infla2 - tx_infla1
        print("Selon la théorie de la PPA relative, la monnaie de départ s'est appréciée de " + str(tx_final) + "% par rapport à la monnaie d'arrivée !")
    elif tx_infla1 == tx_infla2 :
        print("Selon la théorie de la PPA relative, la monnaie de départ ne s'est ni dépréciée ni appréciée par rapport à la monnaie d'arrivée !")

def rendement_titres():
    print("\n\n----\nVous entrez dans l'option 5 !\n => Choix du titre financier par rapport au taux de change entre deux pays.\n----\n")
    tx_int_dep = float(input("Entrez le taux d'interêt d'un titre dans la monnaie domestique (ex : 3.99 pour 3.99%): "))
    tx_int_arr = float(input("Entrez le taux d'interêt d'un titre dans la monnaie étrangère (ex : 3.99 pour 3.99%): "))
    
    tx_change_cpt = float(input("Entrez le taux de change sur le marché (ex : 1$ = 6MIN (Notez 6)) : "))
    tx_change_anticipee = float(input("Entrez le taux de change anticipée à X temps (ex : 1$ = 6MIN (Notez 6)) : "))
    
    gain1 = 100 * tx_int_dep
    gain2 = 100 * (tx_int_arr * (tx_change_anticipee/tx_change_cpt))
    if gain1 > gain2 :
        print("Il faut mieux prendre le titre financier dans la monnaie domestique !")
    elif gain2 > gain1 :
        print("Il faut mieux prendre le titre financier dans la monnaie étrangère !")
    elif gain1 == gain2 :
        print("Tu peux prendre n'importe quel titre !")
        
def tx_change_effectif() :
    print("\n\n----\nVous entrez dans l'option 6 !\n => Calculer le taux de change effectif en fonction de X pays.\n----")
    pays = int(input("Selectionez le nombre de pays pour calculer le taux de change effectif : "))
    tx_list = []
    tx_effectif = 0
    for i in range(0,pays):
        print("\n----\nPays numéro " + str(i+1) + "\n----")
        pourcentage = float(input("Entrez le pourcentage de taux de change (si la monnaie s'apprécie = positif/ si la monnaie se déprécie = négatif) (en %) : "))
        tx_list.append(pourcentage)
        tx_effectif = tx_effectif + pourcentage/100
    tx_effectif = (tx_effectif/pays)*100
    if tx_effectif >=0 :
        print("La monnaie s'est apprécié de " + str(tx_effectif) + " % en moyenne par rapport aux autres pays !")
    elif tx_effectif < 0 :
        tx_effectif = tx_effectif - (tx_effectif*2)
        print("La monnaie s'est déprécié de " + str(tx_effectif) + " % en moyenne par rapport aux autres pays !")
    
def ppa():
    print("\n\n----\nVous entrez dans l'option 7 !\n => Voir si une monnaie est sous ou sur-évaluée grâce au taux de change PPA.\n----")
    tx_change_cpt = float(input("Entrez le taux de change sur le marché (ex : 1$ = 6MIN (Notez 6)) : "))
    
    produit1 = float(input("Tapez le prix du panier dans le pays d'origine (sans devises) : "))
    produit2 = float(input("Tapez le prix du panier dans le pays d'arrivée (sans devises) : "))
    taux_ppa = produit2/produit1
    print("Le taux de change PPA entre les deux monnaie est de 1 pour " + str(taux_ppa) + " !")
    diff = taux_ppa - tx_change_cpt
    if diff >= 0 :
        print("La première monnaie (d'origine) est sous-évaluée tandis que la seconde monnaie (arrive) est sur-évaluée !")    
    elif diff < 0 :
        print("La première monnaie (d'origine) est sur-évaluée tandis que la seconde monnaie (arrive) est sous-évaluée !")    
    
    
        
    
fonction_select = [tx_change_bilaterale_reel,tx_change_bilaterale_reel_inverse,change_fixe,tx_inflation_tx_change,rendement_titres,tx_change_effectif,ppa]
