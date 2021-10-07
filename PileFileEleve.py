import os
os.chdir('D:/Dropbox/NSI/TleNSI2021_2022')

from bibliNSI import *

##Exercice 2

"""Programmer les fonctions de l'interface PILE avec des tableaux dynamiques"""

def CreerPile(...):

    return ...

def estVide(...):

    return ...

def empiler(...):

    return ...

def depiler(...):

    return ...

##Partie 2

class Pile:
    def __init__(self):
        self.contenu = None

    def empiler(self,x):

        self.contenu = Cellule(x,self.contenu)

    def estVide(self):
        return self.contenu is None

#Exercice 3
    def __str__(self):


        res = '|'
        l = self.contenu
        while not l is None:
            res = res + str(l.valeur) + '|'
            l = l.suivante
        return res


    def depiler(self):

        if self.contenu is None:
            raise IndexError("Vous dépilez une liste vide !")

        val = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return val


## Exercice 4
"""Programmer la classe Pile2 afin d'encapsuler les fonctions avec les tableaux permettant de créer des instances qui seront des piles"""





##Partie 3


##Exercice 6

"""Programmer les fonctions de l'interface FILE avec des tableaux dynamiques"""

def CreerFile(...):

    return ...

def estVide(...):

    return 

def enfiler(...):

    return 

def defiler(...):

    return


class File:

    def __init__(self):

        self.tete = None
        self.queue = None

    def estVide(self):
        return self.tete is None


    def enfiler(self,x):

        c = Cellule(x,None)

        if self.tete is None:
            self.tete = c

        else:
            self.queue.suivante = c

        self.queue = c






    def defiler(self):

        if self.tete is None:
            raise IndexError("Attention File vide !")
        val = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None

        return val

#Exercice 7

    def __str__(self):


##Exercice 8 : Calculer en polonaise inverse

chaine= '1 2 3 * + 4 *'





def calculPolonaiseInv(ch):
    """"Permet de calculer uen suite d'instruction en chaien de caractères à la façon polonaise inverse"""

    pass






##Exercice 9 : vérification de parenthésage

chaine = 'a(bc)d((efg)hht(t)b)tt'


"""on utilise une structure de pile puisque la parenthse fermante sera associée à la dernièr ouvrante"""
def parenthese1(ch,f):
    """fonction qui renvoie l'indice de la parenthèse ouvrante associée la pa parenthèse fermante d'indice f"""
    pass

print(parenthse1(chaine,11))






def parenthese2(ch):
    """vérifie si la chaine ch est bien parenthésée"""



chaine2 = 'a(bc)d((efg)hhtt)b)tt'
print(parenthese2(chaine2))
