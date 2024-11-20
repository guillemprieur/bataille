from main_cartes import *
def initialisation(nb_joueurs:int=2,joker:bool=False)->list:
    assert type(nb_joueurs)==int,"Nombre impossible de joueurs."
    assert nb_joueurs>=2,"Pas assez de joueurs pour utiliser cette fonction."
    assert type(joker)==bool,"L'argument joker doit être un booléen."
    paquetInitial = PaquetDeCartes()
    if joker:
        paquetInitial.ajouter(Carte(13,0))
        paquetInitial.ajouter(Carte(13,1))
    paquetInitial.battre()
    return paquetInitial.distribuer(nb_joueurs)

def bataille():
    mainsInitiales=initialisation(joker=True)
    mainJoueurI=mainsInitiales[0]
    mainJoueurII=mainsInitiales[1]
    defausseJoueurI=PaquetDeCartes([])
    defausseJoueurII=PaquetDeCartes([])

    listeCartesEnJeu=[]
    while mainJoueurI.calculerTaille()>0 and mainJoueurII.calculerTaille()>0:

        carteJoueurI=mainJoueurI.piocher()
        carteJoueurII=mainJoueurII.piocher()

        print("Voici la carte du bot :")
        print(carteJoueurI)
        listeCartesEnJeu.append(carteJoueurI)

        print("Voici votre carte :")
        print(carteJoueurII)
        listeCartesEnJeu.append(carteJoueurII)

        if carteJoueurI>carteJoueurII:
            for carteTemporaire in listeCartesEnJeu:
                defausseJoueurI.ajouter(carteTemporaire)
            listeCartesEnJeu=[]
            print("Saperlipopette, sa carte est plus grade que la votre, il récupère donc les deux cartes !")
        elif carteJoueurII>carteJoueurI:
            for carteTemporaire in listeCartesEnJeu:
                defausseJoueurII.ajouter(carteTemporaire)
            listeCartesEnJeu=[]
            print("Bravo, vous récuprérez les deux cartes !")
        else:
            print("Bataille ! Une carte de chaqu'une de vos mains sont mises face caché !")
            if mainJoueurI.calculerTaille==0:
                mainJoueurI=defausseJoueurI
            if mainJoueurII.calculerTaille==0:
                mainJoueurII=defausseJoueurII
            if mainJoueurI.calculerTaille()>0:
                carteJoueurI=mainJoueurI.piocher()
                listeCartesEnJeu.append(carteJoueurI)
            if  mainJoueurII.calculerTaille()>0:
                carteJoueurII=mainJoueurII.piocher()
                listeCartesEnJeu.append(carteJoueurI)
        if mainJoueurI.calculerTaille()==0:
            print("On remélange le paquet adverse")
            defausseJoueurI.battre()
            mainJoueurI=defausseJoueurI
            defausseJoueurI=PaquetDeCartes([])
        if mainJoueurII.calculerTaille()==0:
            print("On remélange votre paquet")
            defausseJoueurII.battre()
            mainJoueurII=defausseJoueurII
            defausseJoueurII=PaquetDeCartes([])
    if mainJoueurI.calculerTaille()==0:
        print("Bravo ! Vous avez gagné !")
    else:
        print("Flute, une prochaine fois peut-être...")
bataille()