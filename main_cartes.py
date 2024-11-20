class Carte:
    """
    Cette class définie une carte spécifique de jeu d'un jeu de 54 cartes, voici les tableaux d'équivalence :
    ------------------------------------------          ------------------------------------------
    ||numérotation interne | valeur désignée||          ||numérotation interne | couleur désignée||
    ||--------------------------------------||          ||---------------------------------------||
    ||--------------------------------------||          ||---------------------------------------||
    ||           0         |       2        ||          ||           0         |        ♥        ||
    ||--------------------------------------||          ||---------------------------------------||
    ||           1         |       3        ||          ||           1         |        ♦        ||
    ||--------------------------------------||          ||---------------------------------------||
    ||           2         |       4        ||          ||           2         |        ♠        ||
    ||--------------------------------------||          ||---------------------------------------||
    ||           3         |       5        ||          ||           3         |        ♣        ||
    ||--------------------------------------||          -------------------------------------------
    ||           4         |       6        ||
    ||--------------------------------------||
    ||           5         |       7        ||
    ||--------------------------------------||
    ||           6         |       8        ||
    ||--------------------------------------||
    ||           7         |       9        ||
    ||--------------------------------------||
    ||           8         |       10       ||
    ||--------------------------------------||
    ||           9         |       J        ||
    ||--------------------------------------||
    ||           10        |       D        ||
    ||--------------------------------------||
    ||           11        |       K        ||
    ||--------------------------------------||
    ||           12        |       A        ||
    ||--------------------------------------||
    ||           13        |     Joker      ||
    ------------------------------------------
    """
    def __init__(self,valeur:int,couleur:int):
        self.identifiant = (valeur,couleur)
        if self.identifiant[0] == 13:
            listeDeCouleurs = ["rouge","noir"]
            self.representationTxt = "joker "+listeDeCouleurs[self.identifiant[1]]
            self.representationAscii = "┌─────────┐\n│         │\n│         │\n│         │\n│         │\n│         │\n└─────────┘"
            self.representationSemiAscii = "┌─────────┐\n│         │\n│         │\n│         │"
        else:
            listeDeCouleurs = ["Coeur","Carreau","Pique","Trefle"]
            listeDeValeurs = ["Deux","Trois","Quatre","Cinq","Six","Sept","Huit","Neuf","Dix","Valet","Dame","Roi","As"]
            self.representationTxt = listeDeValeurs[self.identifiant[0]]+" de "+listeDeCouleurs[self.identifiant[1]]
            listeDeValeurs = [" 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"," J"," Q"," K"," A"]
            listeDeCouleurs = ['♥','♦','♠','♣']
            self.representationAscii = f"┌─────────┐\n│{listeDeValeurs[self.identifiant[0]]}       │\n│         │\n│    {listeDeCouleurs[self.identifiant[1]]}    │\n│         │\n│      {listeDeValeurs[self.identifiant[0]]} │\n└─────────┘"
            self.representationSemiAscii = f"┌─────────┐\n│{listeDeValeurs[self.identifiant[0]]}       │\n│         │\n│    {listeDeCouleurs[self.identifiant[1]]}    │"
    def __str__(self)->str:
        return self.representationAscii
    def __lt__(self,other)->bool:
        assert isinstance(other,Carte),"Impossible de comparer une carte avec autre chose."
        return self.identifiant[0]<other.identifiant[0]
    def __gt__(self,other)->bool:
        assert isinstance(other,Carte),"Impossible de comparer une carte avec autre chose."
        return self.identifiant[0]>other.identifiant[0]
    def __eq__(self,other)->bool:
        assert isinstance(other,Carte),"Impossible de comparer une carte avec autre chose."
        return self.identifiant[0]==other.identifiant[0]
    def __ne__(self,other)->bool:
        assert isinstance(other,Carte),"Impossible de comparer une carte avec autre chose."
        return self.identifiant[0]!=other.identifiant[0]

class PaquetDeCartes:
    """Cette class définie un ensemble de cartes de jeu d'un jeu de 54 cartes."""
    def __init__(self,listeDeCartes:list=None):
        if listeDeCartes==None:
            self.paquet=[]
            for couleur in range(4):
                for valeur in range(13):
                    self.paquet.append(Carte(valeur,couleur))
        else:
            assert type(listeDeCartes) == list,"Mauvais type : pour créer un paquet de cartes il faut fournir une liste en entrée."
            assert all(isinstance(objet,Carte) for objet in listeDeCartes),"Au moins un élément de la liste fournie n'est pas une carte."
            self.paquet = listeDeCartes
        self.affichage = ""
        if len(self.paquet)>0: 
            for carte in self.paquet[:len(self.paquet)-1]:
                self.affichage += "\n" + carte.representationSemiAscii
            self.affichage += "\n" + self.paquet[-1].representationAscii
    def __str__(self):
        return self.affichage
    def calculerTaille(self):
        """
        Renvoie le nombre de cartes présentes dans un paquet.
        """
        return len(self.paquet)
    def battre(self):
        """
        Permet de mélanger un jeu de carte de manière parfaitement aléatoire.
        """
        from random import shuffle
        shuffle(self.paquet)
    def piocher(self):
        """
        Permet de piocher la carte du dessus du paquet (tout en prennant soin de la supprimer du paquet).
        """
        if len(self.paquet)==0:
            return None
        carte=self.paquet[0]
        self.paquet.pop(0)
        return carte
    def ajouter(self,carte):
        """
        Permet d'ajouter une carte en dessous du paquet.
        """
        assert isinstance(carte,Carte),"Il est impossible d'ajouter autre chose qu'une carte à un paquet de cartes."
        self.paquet.append(carte)
    def distribuer(self,n:int)->list:
        """
        permet de séparer le paquet de cartes en un nombre n de paquets différents.
        """
        assert type(n)==int,"Mauvais type : pour distribuer des cartes il faut fournir un entier en entrée."
        assert n<=len(self.paquet),"Le paquet ne peux être distribué en "+str(n)+" part car il n'y a pas assez de cartes dans le paquet pour cela."
        assert n>=1,"Le paquet ne peux être distribué en "+str(n)+" part ce nombre est inférieur à 1."
        listeDePaquets=[]
        for joueur in range(n):
            paquetInter=[]
            for i in range(len(self.paquet)):
                if i%n==joueur:
                    paquetInter.append(self.paquet[i])
            listeDePaquets.append(PaquetDeCartes(paquetInter))
        return listeDePaquets
