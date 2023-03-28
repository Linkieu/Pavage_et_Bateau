# -*- coding: utf-8 -*-
"""
#FICHIER SECONDAIRE DU PROJET PAVAGE AVANCE EN NSI / Par Matthieu


OBJECTIF DE GRAND_TRAPEZE.PY:

    Reprend le principe du projet pavage simple, mais ne dessine pas le
    triangle à droite (triangle B) pour n==nmax.
    Ainsi, il fait juste un grand trapèze composé de 3 triangles
    (eux mêmes composés de 4 triangles)


    Ce fichier sera appelé par le fichier .py mère: projet_tri_force_avancer.py.


INFORMATION:
    La fonction 'trapeze(t)' est similaire à celle de Samuel.
    Nous avons réfléchi ensemble au projet, même si nous avons codé séparément.
"""

from turtle import *
from random import *


def trapeze(t):
    """
    Entrée:
        t : Nombre qui peut être un entier ou un flottant
            Définissant la taille du côté d'un triangle
            (t*2 = grand côté du trapèze)
    Sortie:
        Renvoie rien

    Ce que fait cette fonction:
        Dessine un trapèze en fonction de la taille t.

    Début de fonction:
        Position du curseur: dirigé vers la droite a une position A.
        A l'emplacement de où elle a été appelé

    Fin de fonction:
        Position du curseur: dirigé vers la droite, a la position initial
        (position A)


    Idée de ce que fait la fonction: ▲▼▲
    (le curseur commençant/se terminant en bas à gauche du triangle à gauche)


    """

    #Mise en place pour dessiner le triangle:
    #Choisit une couleur aléatoire à utiliser pour le remplissage.
    rouge, vert, bleu = random(), random(), random()
    fillcolor(rouge,vert,bleu)
    down()
    begin_fill()



    #Trace le trapèze
    forward(t*2) #Plus grand côté du trapèze

    left(120)
    forward(t)

    left(60)
    forward(t) #Trace le côté parallèle au grand côté du trapèze

    left(60)
    forward(t)

    left(120)

    end_fill()
    up()
    return







def mini_triangle(t):
    """
    Entrée:
        t : Nombre qui peut être un entier ou un flottant
            Définissant la taille du côté d'un triangle
    Sortie:
        Renvoie rien

    Ce que fait cette fonction:
        Dessine une sorte de triangle composé de:
            - 1 petit triangle invisible
            - un trapèze

            Cela forme comme un triangle avec un coin manquant, en quelques sorte.

    Début de fonction:
        Position du curseur: dirigé vers la droite à une position A

    Fin de fonction:
        Position du curseur: dirigé vers la droite, à la position initial
        (position A).

    Idée de ce que fait la fonction: (le curseur commençant/se terminant
                                      en bas à gauche du triangle vide.
         ▲
        △▼▲
    """
    width(2)
    up()
    #Mise en place pour la création du trapèze
    forward(t*2)
    left(120)

    #Dessine le trapèze
    trapeze(t)

    #Retourne à la position initial
    right(120)
    backward(t*2)
    color("black")








def fin_triangle(n:int,t):
    """
    Entrée:
        n : Nombre entier
            Indique le nombre de plus petit de triangle sur le côté du triangle.
        t :
            Nombre flottant, qui peut être un entier
            Indique la longueur du côté du triangle

    Sortie:
        Renvoie rien

    Position curseur début/fin: Il commence et s'arrête à l'endroit où la
                                fonction a été appelée.


    Principe:
        Si on a bien travaillé sur un triangle composé de d'autres triangles
        (ou de cas de base), normalement il manque un trapèze.
        Cette fonction sert à placer ce trapèze manquant.

        Le trapèze manquant est de la taille d'un trapèze formant
        le cas de base (donc n=1).
        Pour évitez de faire un trapèze tros gros, si la fonction est appelée
        pour, par exemple, n=3, il va se rappeler jusqu'à atteindre n=1
        et donc la taille t associé.
        Pour ainsi faire un trapèze de bonne taille qui correspond au trou.

        Entre autre:
            n<=1: La fonction peut placer son trapèze manquant,
                  car il est à la bonne taille t.
            n>1: La fonction à besoin de diviser par 2 la taille du trapèze,
                 donc elle se positionne et se rappel pour n-1 et t/2.


    """



    if n<=1: #Si on va bien compléter le plus petit triangle de l'ensemble.
             #(--> Dessine le trapèze manquant)
        trapeze(t)
    else: #Le trapèze manquant est dans un plus petits triangles (triangles n-1)
          #du triangle n,
        #donc il va se rappeler, pour diviser la taille du trapèze, jusqu'à une
        #taille pouvant rentrer dans le petit triangle où manque le trapèze.
        forward(t/2)
        fin_triangle(n-1,t/2)
        backward(t/2)




    return








def reste_du_triangle(n:int,t,nmax):
    """
    Entrée:
        n : Nombre entier
            Nombre définissant le nombre de côté de petits triangles
            qui formeront le triangle.
            Entre autre, ici on va faire un triangle de côté "2 puissance n"
        t : Nombre qui peut être un entier ou un flottant
            Nombre définissant la moitié de la longueur du côté du triangle

        nmax:   Nombre entier
                Nombre définissant le triangle à gauche qui ne va pas apparaître.
                (car déjà tracé par l'autre fichier python, ici on veut juste
                un gros trapèze, qui va s'assembler avec le triangle déjà tracé).

                (Ex: Si projet_tri_force_avancer.py appel la fonction avec n=5,
                 le triangle à gauche pour n=5 ne sera pas tracé par cette fonction.)

    Sortie:
        Renvoie rien

    Ce que fait cette fonction:
        Dessine un trapèze composé de 4 triangles.
        Sauf pour n==nmax où il y en a que 3 du coup.

        Si n<=1:
            Il dessine le cas de base (fonction mini_triangle),
            à la position où il est.

        Sinon:
            Dessine notre triangle, mais pour tracer les petits triangles,
            il fait des appels récursifs.


    Début de fonction:
        Position du curseur: dirigé vers la droite a une position A

    Fin de fonction:
        Position du curseur: dirigé vers la droite, a la position initial
        (position A).

    Dessin de ce que fait la fonction pour n==nmax:
        (le curseur commence/s'arrête en bas à gauche du triangle de gauche
         (triangle transparant))
         ▲
        △▼▲  Le triangle transparant n'est pas tracé.

    Dessin de ce que fait la fonction pour n<nmax:
        (le curseur commence/s'arrête en bas à gauche du triangle de gauche)
         ▲
        ▲▼▲
    """
    speed(0)
    if n<=1: #Cas de base
        mini_triangle(t)
        return
    else:
        #Dessine le premier triangle (celui à gauche)

        up()
        if n!=nmax: #Comme dit plus tôt on veut qu'à la fin de l'exécution
                    #total du programme ça soit un trapèze, et non un triangle.
            reste_du_triangle(n-1,t/2,nmax)

        #Se met en place pour le 2ème triangle
        left(60)
        forward(t)
        right(60)
        forward(t)
        left(120)


        #Dessine le 2ème triangle celui du haut)
        reste_du_triangle(n-1,t/2,nmax)

        #Se met en place pour le 3ème
        left(60)

        #Dessine le 3ème triangle (celui du centre)
        reste_du_triangle(n-1,t/2,nmax)

        #Se met en place
        left(60)

        #Dessine le 4ème triangle (celui à droite)
        reste_du_triangle(n-1,t/2,nmax)

        #Se met en place pour tracer le trapèze manquant
        #(intersection des 3 petits triangles)
        right(120)
        backward(t/2)

        #Trace le trapèze manquant
        fin_triangle(n-1,t/2)

        #Se replace dans la position initial.
        backward(t/2)
        right(120)
        backward(t*2)

        return




