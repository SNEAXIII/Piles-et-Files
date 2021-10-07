class Cellule:
    """ définit la classe Cellule
    valeur : attribut qui contient le premier élément
    suivante : attribut qui contient la suite de la liste"""
    def __init__(self,v,n):
        self.valeur = v
        self.suivante = n

    def __str__(self):
        return str(self.valeur)

    def print_lstc(l,rez=""):
        """fonction qui renvoie une chaine de caractères avec les éléments de la liste"""
        while not l is None: rez, l = rez + str(f"[{l.valeur}] "), l.suivante
        return rez

    def concatenerListe(self, l2):
        if self is None :
            return l2
        return Cellule(self.valeur, self.concatenerListe(self.suivante, l2))



