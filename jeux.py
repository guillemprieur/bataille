#----- importations des class et des modules -----
from main_cartes import *
#----- importations des class et des modules -----


#----- fonctions internes -----
def _initialisation(nb_joueurs:int=2,joker:bool=False)->list:
    assert type(nb_joueurs)==int,"Nombre impossible de joueurs."
    assert nb_joueurs>=2,"Pas assez de joueurs pour utiliser cette fonction."
    assert type(joker)==bool,"L'argument joker doit être un booléen."
    paquetInitial = PaquetDeCartes()
    if joker:
        paquetInitial.ajouter(Carte(13,0))
        paquetInitial.ajouter(Carte(13,1))
    paquetInitial.battre()
    return paquetInitial.distribuer(nb_joueurs)
#----- fonctions internes -----


#----- fonctions de jeux -----
def bataille(pauses:bool=False):
    if pauses:
        from time import sleep
    mainsInitiales=_initialisation(joker=True)
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
        if pauses:
            sleep(1.5)
        if carteJoueurI>carteJoueurII:
            for carteTemporaire in listeCartesEnJeu:
                defausseJoueurI.ajouter(carteTemporaire)
            listeCartesEnJeu=[]
            print("Saperlipopette, sa carte est plus grade que la votre, il récupère donc les cartes en jeu !")
            if pauses:
                sleep(0.5)
        elif carteJoueurII>carteJoueurI:
            for carteTemporaire in listeCartesEnJeu:
                defausseJoueurII.ajouter(carteTemporaire)
            listeCartesEnJeu=[]
            print("Bravo, vous récuprérez les cartes en jeu !")
            if pauses:
                sleep(0.5)
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
            if pauses:
                sleep(1)
        if mainJoueurI.calculerTaille()==0:
            print("On remélange le paquet adverse")
            if pauses:
                sleep(1)
            defausseJoueurI.battre()
            mainJoueurI=defausseJoueurI
            defausseJoueurI=PaquetDeCartes([])
            print(f"Il lui reste {mainJoueurI.calculerTaille()+defausseJoueurI.calculerTaille()} cartes...")
            if pauses:
                sleep(1)
        if mainJoueurII.calculerTaille()==0:
            print("On remélange votre paquet")
            if pauses:
                sleep(0.5)
            defausseJoueurII.battre()
            mainJoueurII=defausseJoueurII
            defausseJoueurII=PaquetDeCartes([])
            print(f"Il vous reste {mainJoueurII.calculerTaille()+defausseJoueurII.calculerTaille()} cartes...")
            if pauses:
                sleep(1)
    if mainJoueurI.calculerTaille()==0:
        print("Bravo ! Vous avez gagné !")
        
    else:
        print("Flute, une prochaine fois peut-être...")
#----- fonctions de jeux -----


#----- exécution par défaut -----
if __name__=="__main__":
    from time import time,sleep
    chrono=time()
    bataille(1)
    print(time()-chrono)
#----- exécution par défaut -----
