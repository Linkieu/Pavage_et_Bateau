#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:15:50 2021

@author: Matthieu
#FICHIER PRINCIPAL DU PROJET PAVAGE AVANCE EN NSI / Par Matthieu

PRINCIPE DE CE FICHIER PYTHON:
    Dessine les triangles qui sont concernés par la présence du trou.
    Sur un triangle n, il va tracer le premier triangle n-1 en fonction des
    coordonnées, mais ça sera grand_trapeze.py qui tracera les 3 autres triangles
    n-1. Pour qu'à la fin, on obtient le triangle n.

    Remarque:
        Si n<=1:la fonction mini_triangle (située dans grand_trapeze.py)
        tracera le triangle invisible + le trapèze.
        La fonction CDB plaçant avant et après l'exécution de cette fonction,
        le curseur.
"""
from turtle import *
from random import *

from grand_trapeze import reste_du_triangle,mini_triangle

#Préparation
reset()
up()
goto(-200,-200)

#Explications pour triangleX
"""
Explication pour les fonctions: triangleA, triangleB, triangleC.

Note:
    l'appelation 'triangleX' désigne l'une des 3 fonctions citées ci-dessus.
    Puisque l'explication, vaudrait aussi bien pour triangleA, que triangleB
    ou triangleC. Cela dépendra de la situation, de quelle fonction sera
    utilisée par le programme.
    Entre autre, dans le cas de 'triangleC', 'triangleX'=='triangleC'.


Entrée:
        n : Nombre entier
            Indique que 'triangleX' est de "2 puissance n"
        t : Nombre qui peut être un entier ou un flottant
            Nombre définissant la moitié de la longueur du côté du triangle
        coord : Désigne les coordonnées du trou.

Sortie:
    Ne renvoie rien.

Objectif:
    - Se déplace à la position adéquate pour former le triangle X
      (vers le haut pour le triangle A, dans le cas de triangleA par exemple).
    - Trace un triangle de côté n-1 triangles, et de taille t/2.
    - Se déplace à la position adéquate pour appeler la fonction
      'reste_du_triangle'. Pour ainsi former le "reste" du triangle.

      Le "Reste" désigne les 3 autres triangles n-1 qui manque pour former n.


#Remarque: La fonction ne revient pas à la position et direction d'origine.
           Mais à une position pour prévoir les futurs déplacement que ferra
           la fonction trianglepro.
"""


#Explications pour retourX
"""
Explications pour les fonctions: retourA, retourB, retourC.
Note:
    L'appelation 'retourX' correspond à la même chose que 'triangleX',
    mais cette fois-ci pour retourA, retourB, retourC.

Entrée:
        t : Nombre qui peut être un entier ou un flottant.
            Nombre définissant la moitié de la longueur du côté du triangle.
        Note: triangleB ne prend aucune entrée.

Sortie:
    Renvoie rien

Objectif:
    Juste après avoir tracé le 'reste' du triangle n, il se replace à
    l'emplacement ET direction où la fonction trianglepro' a été appelé.

#Remarque: La fonction ne revient pas à la position et direction d'origine.
           Car justement, la fonction a seul but de déplacer le curseur, afin
           que ce soit la fonction trianglepro qui revient à sa position
           et direction d'origine !
"""


def triangleA(n,t,coord):
    """
     ▲
    △▽△ Triangle A
    """

    #Se positionne pour faire le triangle A
    left(60)
    forward(t)
    right(60)

    #Trace un triangle
    trianglepro(t/2,coord)

    #Se positionne pour faire le reste du triangle
    right(120)
    backward(t)
    return

def retourA(t):
    #Juste après avoir fait le reste du triangle,
    #se repositionne à la position initial
    forward(t)
    left(120)

    left(60)
    backward(t)
    right(60)
    return




def triangleB(n,t,coord):
    """
     △
    ▲▽△ Triangle B
    """
    #Se positionne pour faire le triangle B -> Ne bouge pas (car déjà bien placé)

    #Trace un triangle
    trianglepro(t/2,coord)

    #Se positionne pour faire le reste du triangle
    #-> Ne bouge pas (car déjà bien placé)
    return

def retourB():
    #Fait surprennant, on est déjà à la position initial !
    #Cette fonction existe malgré tout pour ne pas troubler l'utilisateur s'il
    #essaye de comprendre les étapes de fonctionnement de la fonction
    #trianglepro.
    #Pour ainsi, généraliser le fonctionnement de cette fonction.
    #Ce choix de laisser cette fonction est strictement personnel, et sa
    #suppression n'influe en rien le fonctionnement du programme.
    return




def triangleC(n,t,coord):
    """
     △
    △▽▲ Triangle C
    """
    #Se positionne pour tracer le triangle C
    forward(t)

    #Trace un triangle
    trianglepro(t/2,coord)

    #Se positionne pour faire le reste du triangle
    forward(t)
    left(120)

def retourC(t):
    #Juste après avoir fait le reste du triangle, se repositionne à la position initial
    right(120)
    backward(t*2)






def CDB(n,t,coord):
    """
    La fonction se termine à la même position et direction qu'elle a commencée.


    Entrée:
        n : Nombre entier
            Indique le nombre de petits triangles qui composent le côté.
            Un triangle de "2 puissance n" petits triangles.
        t : Nombre qui peut être un entier ou un flottant
            Nombre définissant la moitié de la longueur du côté du triangle.
        coord : Désigne les coordonnées du trou.

    Sortie:
        Renvoie rien.

    Objectif:
        - Se place pour appeler la fonction mini_tringle
        - Appel la fonction mini_triangle (et trace donc un trapèze)
        - Se replace à la position et direction où la fonction a été appelée.

        Le principe est de placer un trapèze de sorte qu'un trou se forme à
        l'emplacement de la coordonnée.
        Si coord[0]=="B", alors à l'emplacement de triangle B, il y aura rien.
         ▲
        △▼▲ Les triangles colorés représentes le trapèze. Le trou: triangle B.

    """
    if n>1: #La fonction doit-être appelée UNIQUEMENT si n=1. Sinon, on signale
            #le problème:
        print("ATTENTION: Il y a une erreur, la fonction cas de base est appelé, alors que n est trop grand !")
        return

    if coord[0]=="A":
        #Se place.
        right(120)
        backward(t*2)

        #Trace un trapèze et un trou vide, sans contour.
        mini_triangle(t)

        #Se replace à la position initial.
        forward(t*2)
        left(120)

        return
    elif coord[0]=="B":
        mini_triangle(t)
        return
    elif coord[0]=="C":
        forward(t*2)
        left(120)

        mini_triangle(t)

        right(120)
        backward(t*2)
        return
    else:
        print("ATTENTION: Il y a un pronlème de coordonné dans CDB")
        #Cas où la variable "coord" Ne contient pas une liste de lettres








def trianglepro(t,coord):
    """
    Fonction principale du programme.
    La fonction se termine à la même position et direction qu'elle a commencée.


    Entrée:
        t : Nombre qui peut être un entier ou un flottant
            Nombre définissant la moitié de la longueur du côté du triangle
        coord :     Une liste (ou chaîne de caractère, mais qui va être
                               transformée en liste)
                    Coordonnées du trou

    Sortie:
        Ne renvoie rien

    Objectif:
        Trace un triangle n-1 avec un trou.
        Pour tracer les 3 autres triangles n-1 afin de former le triangle n,
        il va devoir appelé la fonction "reste_du_triangle" situé dans
        le fichier python grand_trapeze.py.

        Exemple:
        Avec la récursivité, il va en premier, aller à la position du trou.
        Il va exécuter le cas de base (qui en fonction des coordonnés
        tracera un trapèze ajusté pour former le trou ).
        Puis il dessinera le "reste" (les 3 autres triangles) pour former un
        plus grand triangle.

        Ainsi, on a formé un triangle n-1. Pour former n, il va dessiner le
        "reste" (en appelant encore grand_trapeze.py).
        Ce qui formera un triangle n-1, pour former n, il va dessiner le
        "reste"...
        On peut reconnaître l'aspect récursif du programme.
    """

    #Etape 0: Si c'est une chaîne de caractère, on la transforme en liste.
    if type(coord)==str:
        coord=list(coord)
    assert type(coord)==list, "\nERREUR >>> La variable 'coord' n'est pas une liste.\n'trianglepro' doit être appelée avec 'coord' de type str ou list."
    assert t>0, "\nERREUR >>> La taille du triangle doit être un nombre supérieur à 0.\nLa fonction 'trianglepro' refuse donc de fonctionner."



    """
    n : Nombre entier
    Nombre définissant le nombre de côté de petit qui formeront le triangle.
    Entre autre, ici on va faire un triangle de côté "2 puissance n"
    A noté que n est la taille du tableau. Donc si len(coord)==3, n==3.
    """
    n=int(len(coord))



    if n<=1:
        #1ère étape (A): le Cas de base, si n<=1.
        """
        Nous allons tracer le cas de base qui contiendra le trou:
        """
        CDB(n,t,coord)
        return

    else:
        #1ère étape (B): Premier triangle, si n>1.
        """
        Ici nous partons du principe que n>1.
        Donc que "coord" fait une longueur de 2 (Par exemple: n=2: ["A","A"],
                                                 Ou: n=3: ["B","C","C"]
                                                 car len(["B","C","C"])==3)
        Donc coord[0] nous indique le choix à faire:

        Exemple:    Si coord[0]=="A", alors on éxécute la fonction triangleA.
                    Qui nous positionnera en haut.
        """

        if coord[0]=="A": #Le premier triangle à tracer est le triangle A
            triangleA(n,t,coord[1:]) #Note: la fonction s'occupera directement
                                     #d'envoyer "n-1" et "t/2"
        elif coord[0]=="B": #Le premier triangle à tracer est le triangle B
            triangleB(n,t,coord[1:])
        elif coord[0]=="C": #Le premier triangle à tracer est le triangle C
            triangleC(n,t,coord[1:])

        #2ème étape: Le "reste"
        """
        Nous venons de tracer le premier triangle !
        Maintenant, il faut tracer les 3 autres triangles n-1, pour au final,
        former n. Cette ensemble de 3 triangles sera souvent appelé "le reste".
        Pour cela, on appel reste_du_triangle. Cette fonction est située dans
        grand_trapeze.py.
        """
        reste_du_triangle(n,t,n)

        #3ème étape: Retour à la position inital
        """
        La fonction reste_du_triangle nous a laissé à la position où on l'a
        appelée. Autrement dit, ce n'est pas la position de quand
        la fonction trianglepro a été appelée.

        Ici, en fonction de quel 1er triangle nous avons tracer, nous allons
        suivre un trajet spécifique afin de retourner à la position de départ.

        Exemple:    Si a l'étape 1 (B), nous avons tracé C, nous allons ici
                    exécuté retourC.
        """

        if coord[0]=="A":
            retourA(t)
        if coord[0]=="B":
            retourB() #Note: Cette fonction ne fait rien, il a été préféré de
                      #la laisser malgré tout.
        if coord[0]=="C":
            retourC(t)
        return






def trou_aleatoire():
    """
    Entrée: Aucune
    Sortie: coord
        coord : Un liste de caractère.
                Correspond aux coordonnées du trou.
    Principe: Génère un trou aléatoire dans un triangle de taille aléatoire.
    Affiche: Les caractéristique du triangle.
    """
    n=int(uniform(1,7)) #Nombre aléatoire entre 1 et 7. n, un entier: 1<=n<7.
    coord=[choice(["A","B","C"]) for i in range(n)]
    #Génère un tableau de type list de n éléments aléatoire entre "A","B","C".

    print("---------------------------------------------------------\n"
          "Caractéristique de mon triangle:\n"
          "---------------------------------------------------------\n"
          "- Composé d'un côté de",2**n,"petits triangles\n"
          "- Coordonnées du trou:",coord,"\n"
          "---------------------------------------------------------\n"
          )

    return coord


speed(0)
trianglepro(200,trou_aleatoire())

#Au format triangle(t,coord).

# t pour taille, coord pour coordonné du trou.
# Attention, la fonction ne prend en charge que des str/list pour coord.
# Attention t doit être un nombre supérieur à 0.
