from boi import Cellule

## Exercice 2


def CreerPile():
    return []


def estVide(p):
    if p: return True


def empiler(p, x):
    p.append(x)


def depiler(p):
    return p.pop()


## Partie 2


class Pile:
    def __init__(self):
        self.contenu = None

    def empiler(self, x):
        self.contenu = Cellule(x, self.contenu)

    def estVide(self):
        return self.contenu is None

    def depiler(self):
        if self.contenu is None:
            raise IndexError("Vous dépilez une liste vide !")

        val = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return val

## Exercice 3

    def __str__(self):
        res, l = '| ', self.contenu
        while not l is None:
            res, l = res + str(l.valeur) + ' | ', l.suivante
        return res


## Exercice 4 wip


class Pile2:
    def __init__(self):
        self.contenu = []

    def estVide(self):
        if len(self.contenu) == 0:
            return True
        return False

    def enfiler(self, f, x):
        f.insert(0, x)

    def enfiler2(self, f, x):
        f.append(x)

    def defiler(self, f):
        return f.pop()

    def defiler2(self, f):
        return f.pop(0)


## Partie 3

## Exercice 6 wip

# c'est pas l'exo 6, mais la préparation pour la suitre


class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def estVide(self):
        return self.tete is None

    def defiler(self):
        if self.tete is None:
            raise IndexError("Attention File vide !")
        val = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return val

    def enfiler(self, x):
        c = Cellule(x, None)
        if self.tete is None:
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c


## Exercice 7

    def __str__(self, rez="["):
        l = self.tete
        while l is not None:
            rez += str(f"{l.valeur}")
            if l.suivante is not None:
                rez += ", "
            l = l.suivante
        rez += "]"
        return rez

file1 = File()
for a in [1, 3, 7, -5]:
    file1.enfiler(a)

## Exercice 8


def calc(signe, x, y):
    if signe == "*":
        return int(x) * int(y)
    elif signe == "+":
        return int(x) + int(y)


def poloInverse(ch):
    pile_1 = Pile()
    for a in ch.split(' '):
        if a in ("*", "+"):
            a = calc(a, pile_1.depiler(), pile_1.depiler())
        pile_1.empiler(a)
    return pile_1.depiler()


chaine = '1 2 3 * + 4 *'
#print(poloInverse(chaine))

## Exercice 9

chaine = 'a(bc)d((efg)hht(t)b)tt'
"""on utilise une structure de pile puisque la parenthèse fermante sera associée à la dernièr ouvrante"""


def parenthese1(ch, f):
    """fonction qui renvoie l'indice de la parenthèse ouvrante associée à la parenthèse fermante d'indice f"""
    pile1 = Pile()
    for a, x in enumerate(ch):
        if x == "(":
            pile1.empiler(a)
        elif a == f and x == ")":
            return pile1.depiler()
        elif x == ")":
            pile1.depiler()


print(parenthese1(chaine, 11))


def parenthese2(ch):
    pile2 = Pile()
    for a in ch:
        if a == "(": pile2.empiler(a)
        elif a == ")" : 
          if not pile2.estVide(): pile2.depiler()
          else : return False
    if pile2.estVide(): return True
    return False


chaine2 = '(()()()()(()()))'
print(parenthese2(chaine2))