#setheading(angle)  -> fixe langle à ?????? 0= par défaut


#DEVOIR DE MATTHIEU

#Note: "lt" signifie "left", "rt" signifie "right", ce sont des abréviation que
#j'ai trouvé sur internet lors d'une recheche Python (avant ce travail).

#Note 2: j'ai trouvé les commandes "random" (de from random import *) sur
#internet. randint(a, b) choisit un nombre entier aléatoire entre les nombres
#a et b (a et b étant compris).

#Note 3: Tout comme "random", j'ai trouvé "time" sur internet. Il me permet de
#faire un temps d'attente durant mon script (pour la partie Bonus).

#Note 4: Si vous exécuter le fichier python, le script du Bonus s'exécutera.
#On y retrouve le même script que pour le dernier exercice, mais j'ai rajouté
#un cadre, de l'eau, un soleil, un logo.

from turtle import *
from math import *
from random import *
import time
reset()
speed(0)
up()







#-------------------------------------------------------------------------------

a=1
#print(a)
#1 LA SIGNATURE (3)


#L'énoncé me demande de faire une fonction sans argument. Mais pour l'exercice 5
#j'ai besoin d'adapter la taille des lettres à mon bateau.
#J'ai donc inséré comme
#argument la variable (a) afin qu'elle soit associé à la taille de mon bateau.
#La création de la variable (a) est demandé dans l'exercice 5.

#Pour qu'aucun message d'erreur apparaisse si on veut exécuter le script sans
#passer par la fonction "bateau", dès le début j'indique que a=1 afin qu'un
#simple "SIGNATURE(a)" marche, avec les valeurs imaginés au début du projet.
#J'ai placé le "a=1" avant l'exercice, afin que ce type de problème ne se
#produise pas dans les prochains exercices.


#Toute mes valeurs par défaut sont multipliés par (a). Si "a=2", mes lettres
#seront 2 fois plus grande.
#Si "a=0.5", mes lettres auront leur taille divisé par 2.
#Elles seront donc proportionnel à "a" (donc avec la taille de mon bateau).

def SIGNATURE(a,lettre):
    up()
    #MA
    if lettre==1:
        #Pour M
        down()
        lt(90)
        forward(100*a)
        #Si a=1, la longueur sera 100. Si a=2, la longueur sera 200, etc. ↑
        rt(135)
        forward(60*a)
        lt(90)
        forward(60*a)
        rt(135)
        forward(100*a)

        #Espace
        up()
        lt(90)
        forward((20)*a)

    #Maintenant le A
    down()
    #Fonction créant le A (vu que je vais l'appeller 2 fois, pour simplifier le
    #script).
    def A():
        lt(75)
        forward(100*a)
        rt(150)
        forward(100*a)
        #### Trait du milieux du A
        backward((50)*a)
        lt(75)
        backward((25)*a)
        #### Retour en arrière
        forward((25)*a)
        rt(75)
        forward((50)*a)

    if lettre==1:
        #Appel du A
        A()
        #Espace
        up()
        lt(75)
        forward((20)*a)

    #FA
    #Pour F
    down()
    lt(90)
    forward(100*a)
    rt(90)
    forward(60*a)
    backward(60*a)
    rt(90)
    forward(50*a)
    lt(90)
    forward((40)*a)
    backward((40)*a)
    rt(90)
    forward(50*a)

    #Espace
    lt(90)
    up()
    forward(80*a)
    down()

    #A
    #Appel du A
    A()

    #Résultat: MAFA

    #Remise à la position d'origine
    lt(75)
    up()
    backward(308*a)
    #308 est la longueur de mon texte.

#SIGNATURE(a) #Appellez la fonction


#-------------------------------------------------------------------------------


#2 UNE FONCTION RECTANGLE (2)

#Pour commencer, le logiciel va faire un rectangle de couleur "couleur" et le
#remplir.
#Si il y a aucune couleur de choisit, le rectangle ne sera pas remplis.
def RECTANGLE(l,h,couleur,cadre):
    color(couleur)
    begin_fill()
    down()
    #Boucle permettant de créer le rectangle:
    for i in range (2):
        forward(l)
        lt(90)
        forward(h)
        lt(90)
    end_fill()
#Maintenant, il va faire le contour du rectangle si "cadre=1".La couleur par
#défaut du est le noir. Car si c'était "couleur", on ne distinguerais pas le
#contour avec l'intérieur du rectangle.
    if cadre==1:
        for i in range (2):
            #Même boucle que la première, mais avec des paramètres en plus:
            width(2)
            color("black")
            forward(l)
            lt(90)
            forward(h)
            lt(90)
        return
    else:
        return
#RECTANGLE(40,50,"red",1) #Appellez la fonction


#-------------------------------------------------------------------------------


# 3 LES DRAPEAUX (10)

#3.1 LA FONCTION drapeauD (2)

def drapeauD(l,h):
    #Ici, on me demande de faire un drapeau composé de 3 rectangles:
    #1 jaune, puis 1 bleu et pour finir 1 jaune de même taille que le premier
    #rectangle jaune. Ils ont tous le contour noir.



    #Création du 1er rectangle jaune avec contour.
    RECTANGLE(l,h/5,"yellow",1)
    #Mise en place puis création du rectangle bleu avec contour.
    lt(90)
    forward(h/5)
    rt(90)
    RECTANGLE(l,(h/5)*3,"blue",1)
    #Mise en place puis création du 2ème rectangle jaune avec contour.
    lt(90)
    forward((h/5)*3)
    rt(90)
    RECTANGLE(l,h/5,"yellow",1)
    #Remise à la position d'origine
    up()
    rt(90)
    forward((h/5)*4)
    lt(90)
    return
#drapeauD(100,150) #Appellez la fonction

#-------------------------------------------------------------------------------

#3.2 LA FONCTION DrapeauG (2)
def drapeauG(l,h):
    #Ici, on me demande de faire 1 rectangle jaune avec un contour, puis un
    #rouge aussi avec un contour, le tout 3 fois.
    #Comme pour les prochains drapeaux, j'ai du mal à voir si tout les
    #rectangles ont besoin d'un contour. Je suppose qu'ils ont tous besoin
    #d'un contour.
    #Sinon, ici j'aurais fait la même chose (mais sans contour), puis un
    #rectangle final, non remplis, avec juste un contour noi à faire.
    #Il sera juste "encadré" par le noir.


    #Voici une boucle s'exécutant 3 fois (i=0 puis i=1 puis i=2).
    #Car il y a 3 fois le même motif qui est demandé.
    for i in range(3):
        #Création d'un rectangle jaune avec contour.
        RECTANGLE(l/6,h,"yellow",1)
        #Se prépare au prochain rectangle
        forward(l/6)
        #Création d'un rectangle rouge avec contour.
        RECTANGLE(l/6,h,"red",1)
        #Se prépare au prochain rectangle
        forward(l/6)
        #Fin
    #Remise à la position d'origine
    up()
    backward(l)
    return
#drapeauG(150,100) #Appellez la fonction

#-------------------------------------------------------------------------------

#3.3 LA FONCTION DrapeauA (2)

def drapeauA(l,h):
    #Ici, on me demande en quelque sorte
    #de faire un rectangle blanc avec contour noir, puis
    #2 triangles rectangles rouge avec contour.
    #Et si il y a un espace entre le rectangle et l'ensemble des 2 triangles,
    #il faut que ce sorte de rectangle formé soit remplis de rouge.



    #Initialisation des valeurs
    triangles=0
    color("black")
    #Construction du rectangle blanc avec contour
    down()
    RECTANGLE(l/2, h,"white",1)
    up()
    forward(l/2)
    #Préparation à la création des 2 triangles
    color("red")
    down()
    begin_fill()
    forward(l/2)
    lt(135)
    #variable triangles:
    triangles=(h/2)**2+(h/2)**2
    #Explication de pourquoi cette variable se présente comme cela:
    #Je veux connaître l'hypoténuse de mon triangle.
    #Pour cela je fais le théorème de Pythagore: a²+b²=c².
    #Ici, a=l/2 et b=h/2
    #Pour dreapeauA(100,100) → a=50 et b=50.
    #Donc: 50²+50²=triangles soit triangles=5000.
    #Pour une distance correcte, je fait la racine carré de "triangles".
    #Pour drapeauA(100,100), ma figure est celle dont je veux.
    #
    #Mais pour drapeauA(200,120), je m'aperçois que l'hypoténuse est trop grand.
    #J'en ai donc déduit qu'ici il ne faut pas reprendre le théorème mais s'en
    #inspiré. Ainsi, pour essayer j'ai fais b²+b²=triangles
    #Et ma figure est bien reproduite pour drapeauA(200,100), drapeauA(100,100)
    #Cela marche parfaitement si: l<h .
    #
    # ► la variable "triangles=(l/2)**2+(h/2)**2" calcule l'hypoténuse.

    #La fonction "tria()" fait 2 triangles d'affilé:
    def tria():
        forward(sqrt(triangles))
        rt(90)
        forward(sqrt(triangles))
        lt(135)
        forward(l/2)
        lt(90)
        forward(h)
        lt(90)
    #Demande à la fonction de faire un triangle puis de terminé le remplissage:
    tria()
    end_fill()
    #Recommence, à quelques paramètres près afin de faire les contours noirs:
    color("black")
    forward(l/2)
    lt(135)
    tria()
    #Remise à la position d'origine:
    up()
    backward(l/2)
    return

#drapeauA(200,120) #Appellez la fonction.

#-------------------------------------------------------------------------------

#3.4 La fonction drapeau0 (2)
from math import *
def drapeau0(l,h):
    #Création d'un rectangle rouge
    RECTANGLE(l,h,"red",0)
    #Calcule de l'hypoténuse avec le théorème de pythagore a²+b²=c²
    pythagore=sqrt(l**2+h**2)
    #Préparation avant de tracé le triangle
    color("yellow")
    begin_fill()
    lt(90)
    forward(h)
    rt(90)
    #Calcule l'angle de l'hypoténuse par rapport à l'opposé.
    rt(degrees(asin(h/pythagore)))
    #Tracé du triangle rectangle avec un remplissage jaune
    forward(pythagore)
    end_fill()
    #Préparation à la création des contours
    lt(degrees(asin(h/pythagore)))
    backward(l)
    #Création des contours du rectangle puis fin de la fonction.
    RECTANGLE(l,h,"",1)
    return
#drapeau0(150,80) #Appellez la fonction.

#-------------------------------------------------------------------------------

#3.5 La fonction drapeauI (2)

def drapeauI(l,h):
    #Création d'un rectangle blanc avec contour
    RECTANGLE(l,h,"white",1)
    #Le script après if/else est le même pour l>=h ou non, seul les valeurs
    #change. Donc ici, if sert à asigné 2 variables commune avec des valeurs
    #différentes en fonction de si l>=h ou non.
    if l>=h:
        g=h
        p=l/2-h/4
    else:
        g=l
        p=l/4
    #Préparation à la création de notre cercle.
    up()
    forward(l/2+g/4)
    lt(90)
    forward(h/2)
    #Création de notre cercle rouge.
    color("red")
    begin_fill()
    down()
    circle(g/4,360)
    end_fill()
    up()
    #Remise à la place d'origine
    backward(h/2)
    rt(90)
    backward(l-p)
    color("black")
    return
#drapeauI(200,100) #Appellez la fonction.


#-------------------------------------------------------------------------------


#4 LE BATEAU ET LES DRAPEAU (5)



from math import *
def bateau(a):

    #####ETAPE A: VERIFICATION DE LA VALEUR a ----------------------------------

    if a<=0:
        print("ERREUR - Votre nombre doit être supérieur à 0 !")
        return

    ####ETAPE B: LE TRAPEZE DU BÂTEAU ------------------------------------------

    #Préparation à la création du bateau.
    up()
    goto(-50,-200)
    #Appel la fonction SIGNATURE pour signé le bateau
    down()
    SIGNATURE(a,1)
    #Préparation au tracé du bas du bateau (se déplace de 25*a vers le bas)
    rt(90)
    up()
    forward(25*a)
    lt(90)
    down()
    #Trace la distance des lettres M et A (308*a) puis 400 pour faire le bout.
    forward((308*a)+400*a)
    #Trace le bord du bateau
    lt(45)
    forward(220*a)
    lt(135)
    #Ici, on doit connaître la longueur de l'adjacent, pour cela on fait le
    #cosinus de 45 fois la distance de l'hypoténuse.
    ok=(cos(radians(45))*(220*a))
    #(aide): Imprime la variable ok
    print(ok)
    #Trace 2 fois ok (pour les 2 bords, celui à gauche et à droite) +
    #la longueur du texte MAFA, et la distance qui sépare M du bord droit.
    #Ou A du bord Gauche (donc 2 fois cette longueur).
    forward(ok*2+(308*a+800*a))
    #Trace le 2ème bord du bateau
    lt(135)
    forward(220*a)
    lt(45)

    ####ETAPE C : LE MÂT -------------------------------------------------------

    #Préparation de la création du mât du bâteau.
    forward(554*a)
    up()
    lt(90)
    #(préparation), on veut connaître la distance qui sépare le bas, au planché
    #du bateau (au pied du mât), pour cela, on calcule le sinus du premier bord.
    #Soit la distance de la longueur inconnu de notre triangle rectangle (on
    #connaît 2 longueur (hypoténuse + celui qu'on avait calculé) sur 3.
    forward(sin(radians(45))*(220*a))
    down()
    #Création du mât du bâteau
    forward(100*a)

    ####ETAPE D: LA VOILE ROUGE ------------------------------------------------

    #Préparation à la création de la voile rouge.
    begin_fill()
    color("red")
    #Ici se trouve la fonction tria qui va tracé le triangle (la voile).
    #Je voulais faire un triangle rouge, puis faire les contours sur ce même
    #triangle. Ainsi, la fonction va me permettre de l'appelé 2 fois. Pour
    #remplir de rouge le triangle, puis pour faire les bord.
    def tria():
        forward(600*a)
        lt(135)
        #Je veux que ma longueur de la voile sur le mât soit de 600.
        #Et que celui-si s'étend de 600 vers là gauche.
        #Le problème est qu'il me faut l'hypoténuse.
        #Ainsi, à l'aide du théorème de Pythagore, je fois a²+b²=pythagore avec
        #A= 600*a et B= 600*a. Ce qui nous donne en python:
        pythagore=(600*a)**2+(600*a)**2
        #Je trace donc l'hypoténuse:
        forward(sqrt(pythagore))
        #Je trace maintenant le bas de ma voile, soit le côté pas encore tracé.
        lt(135)
        forward(600*a)
        lt(90)
    #J'appel ma fonction tria() avec begin_fill() et end_fill() afin de la
    #remplir de couleur rouge (rouge choisit juste au dessus de la fonction).
    tria()
    end_fill()
    #Préparation au contour.
    color("black")
    width(2)
    #Création du contour. 2ème appel à tria()
    tria()

    ####ETAPE E: GUIRLANDE DE DRAPEAU ------------------------------------------

    #Préparation à la guirlande de drapeau (remonte le mat, puis se dirige).
    forward(600*a)
    rt(135)
    width(1)
    #Voici ce que je vais faire:
    #Etape 1:
    #En premier lieu, je vais choisir mon nombre de drapeau à tracé.
    #Ce nombre sera entre 1 et 6 (2, 3, 4, 5, 6)
    #Ce nombre sera assigné à la variable "nbdrapeau"
    #Etape 2:
    #Par la suite, je calculerais à l'aide du théorème de Pythagore, la longueur
    #de l'hypoténuse. Ce nombre sera assigné à "pythadrapeau"
    #Etape 3:
    #Juste après cette variable, je ferrais avancé mon curseur de
    #forward(distance).
    #Et la variable distance fera: pythadrapeau/(nbdrapeau*2+1)
    #Car la largeur d'un drapeau est ce calcule (↑).

    #Le +1 correspond au premier espace, entre le mât et le premier drapeau.
    #Pour le "nbdrapeau*2":
    #Etape 4:
    #Il y aura une boucle qui dira:
    #   -Tracé 1 drapeau
    #   -Tracé 1 espace de même largeur que le drapeau
    #Cette boucle fera varier i dans la rangé de (nbdrapeau).
    #Le problème est qu'1 boucle va faire une distance de 2 largeur de drapeau.
    #Pour résoudre ce problème, on va multiplier par 2 nbdrapeau (+ 1) et
    #et diviser pythadrapeau.


    #En résumer:
    # → +1 correspond au premier espace à tracé
    # → nbdrapeau*2 correspond à (nbdrapeau) + espace après chaque drapeau.
    # ► Donc: pour nbdrapeau = 5
    # 5*2 = 10.                 5 + 5 = 10 (nbdrapeau + espaces = nbdrapeau*2).
    #("+1" sera pris en compte pour la distance total).

    #Etape 1:
    nbdrapeau=(randint(2,5))
    print(nbdrapeau) #sert à donné le nombre de drapeau qui a été tiré

    #Etape 2:
    #mât = 700, distance mât → bord = 554+ok ((distance texte/2 + 400)*a + ok).
    pythadrapeau=sqrt((700*a)**2+(554*a+ok)**2)
    print(pythadrapeau) #aide

    #Etape 3:
    distance=(pythadrapeau/(nbdrapeau*2+1))
    forward(distance)
    #speed(3)

    #Etape 4:

    def fin():
        #Dès que la création d'un drapeau est terminé, cette fonction s'exécute.
        #Afin de se préparer à la création d'un nouveau drapeau.
        lt(90)
        width(1)
        down()
        color("black")
        #Il se met au début du drapeau, donc il doit parcourir la distance
        #1 fois pour arriver au bout du drapeau, puis une 2ème fois afin
        #que le nouveau drapeau puisse se créer à cette emplacement:
        forward(distance*2)

    for i in range(nbdrapeau):
        #missingno est un nombre aléatoire entre 1 et 5 compris.
        missingno=randint(1,5)
        rt(90)
        if missingno==1:
            drapeauD(distance*1.5,distance)
            fin()
            #(si missingno==1, alors le drapeauD sera dessiné)
        if missingno==2:
            drapeauG(distance*1.5,distance)
            fin()
            #(si missingno==2, alors le drapeauG sera dessiné)
        if missingno==3:
            drapeauA(distance*1.5,distance)
            fin()
            #(si missingno==3, alors le drapeauA sera dessiné)
        if missingno==4:
            drapeau0(distance*1.5,distance)
            fin()
            #(si missingno==4, alors le drapeau0 sera dessiné)
        if missingno==5:
            drapeauI(distance*1.5,distance)
            fin()
            #(si missingno==5, alors le drapeauI sera dessiné)

    #### FIN DE LA FONCTION BATEAU ---------------------------------------------

#bateau(float(input("Entrez la taille de votre bâteau:")))
#bateau(0.4)


#-------------------------------------------------------------------------------


#5 BONUS

#Explication de mon idée:
#J'aimerais faire un sorte de tableau (repprenant mon bâteau "Mafa") avec juste
#avant un écran avec un logo "MAfa" introduant mon bateau.
#Je commence donc pas créer mon logo MAfa (qui est comme une marque de bateau)
#avec juste après un "présente" qui apparait dessus.
#Comme si la marque voulait présenter son nouveau bateau, le "Mafa".
#Après avoir terminé la création du logo, celui-ci devra rester 2 secondes à
#l'écran, avant de disparaître au profit de la création du bateau.
#Une fois le bateau créer, le logo "MA" apparait pour montrer qu'il appartient
#à "l'entreprise" MAfa.
#Pour que ça soit plus joyeux, je vais faire un cadre avec un petit soleil
#jaune avec ses rayons qui vont illuminer la mer où se trouve le bateau.
#Juste après il créer l'eau (qui représente la mer où dessus il y a le bateau)
#et réparer le cadre afin de conclure ce script.













def bonus(a):
    #Fonction créant la lettre M:
    def M(a):
        #Création de la partie bas du M.
        print(a)
        speed(0)
        down()
        width(2)
        #MoitierBas du M
        forward(125*a)
        up()
        forward(125*a)
        #
        lt(130)
        down()
        forward(150*a)
        lt(125)
        forward(120*a)
        #
        setheading(0)
        up()
        forward(128*a)
        down()
        #
        lt(50)
        forward(150*a)
        lt(55)
        backward(120*a)
        setheading(0)
        forward(125*a)
        #
        #Création du côté droit du M
        lt(105)
        forward(371*a)
        #Création du haut du M
        rt(55)
        backward(240*a)
        lt(80)
        forward(240*a)
        #Création du côté gauche du M
        lt(124.5)
        forward(370*a)
        setheading(0)
        up()
        return

    #Fonction créant la fonction A:
    def A(a):
        #Mise en place pour faire le A
        forward(250*a)
        lt(129)
        forward(150*a)
        lt(118)
        #Création du A (par le côté gauche)
        color("red")
        begin_fill()
        down()
        backward(250*a)
        #Création du côté droit
        lt(45)
        forward(250*a)
        #Création du reste du A
        lt(68)
        backward(50*a)
        up()
        backward(90*a)
        down()
        end_fill()
        color("white")
        begin_fill()
        backward(50*a)
        forward(50*a)
        lt(249)
        backward(80*a)
        lt(113)
        forward(30*a)
        lt(111)
        backward(83*a)
        end_fill()
        color("white")
        rt(111)
        forward(20*a)
        up()
        #
        lt(111)
        forward(120*a)
        rt(111)
        begin_fill()
        down()
        backward(40*a)
        lt(60)
        forward(40*a)
        rt(120)
        forward(40*a)
        end_fill()
        up()
        #####
        #Retour à la position initial avant la création du M
        color("black")
        lt(60)
        backward(278*a)
        lt(90)
        backward(215*a)
        rt(90)
        return
    def presente(a):
        #Mise en place pour pouvoir faire le "Présente" et son fond noir.
        color("red")
        lt(90)
        forward(215*a)
        rt(90)
        forward(278*a)
        rt(60)
        ####
        #Création du cadre remplis noir.
        forward(20*a)
        setheading(0)
        color("black")
        begin_fill()
        down()
        backward(160*a)
        lt(90)
        backward(50*a)
        lt(90)
        backward(260*a)
        lt(90)
        backward(50*a)
        lt(90)
        backward(260*a)
        rt(90)
        #
        #Mise en place pour écrire le "Présente"
        up()
        end_fill()
        color("white")
        forward(10*a)
        lt(90)
        forward(10*a)
        down()
        #Présente
        #Création du "P" de Présente
        forward(20*a)
        rt(90)
        forward(10*a)
        rt(90)
        forward(20*a)
        rt(90)
        forward(10*a)
        backward(30*a)
        rt(90)
        up()
        forward(30*a)
        #pRésente
        #Création du "R" de Présente
        down()
        lt(90)
        forward(30*a)
        rt(90)
        forward(20*a)
        rt(90)
        forward(10*a)
        rt(90)
        forward(20*a)
        rt(45)
        pythaB=sqrt((20*a)**2+(20*a)**2)
        backward(pythaB)
        lt(45)
        up()
        backward(10*a)
        down()
        #prEsente
        #Création du "E" de Présente
        #Je décide de faire une fonction afin de la réappeler si j'ai besoin de
        #faire un E plus loin.
        def E():
            rt(90)
            forward(30*a)
            rt(90)
            forward(20*a)
            backward(20*a)
            lt(90)
            backward(15*a)
            lt(90)
            backward(10*a)
            forward(10*a)
            lt(90)
            forward(15*a)
            lt(90)
            forward(20*a)
            up()
            forward(10*a)
        E()
        #préSente
        #Création du "S" de Présente
        down()
        forward(20*a)
        lt(90)
        forward(15*a)
        lt(90)
        forward(20*a)
        rt(90)
        forward(15*a)
        rt(90)
        forward(20*a)
        up()
        rt(90)
        forward(30*a)
        lt(90)
        forward(10*a)
        #Création du "E" de Présente (appel de la fonction E)
        #PrésEnte
        down()
        lt(180)
        E()
        #PréseNte
        #Création du "N" de Présente
        down()
        lt(90)
        forward(30*a)
        rt(145)
        forward(37*a)
        lt(145)
        forward(30*a)
        up()
        rt(90)
        forward(10*a)
        #présenTe
        #Création du "T" de Présente
        down()
        forward(20*a)
        backward(10*a)
        rt(90)
        forward(30*a)
        lt(90)
        up()
        forward(20*a)
        #présentE
        #Création du "E" de Présente (appel de la fonction E)
        lt(180)
        down()
        E()
        #
        #Retour à la position d'origine du logo MA
        color("white")
        backward(375*a)
        rt(90)
        forward(168*a)
        lt(90)
        return
    #"""
    #logo MAFA
    #Mise en place pour créer le logo MA
    up()
    goto(-250*a,-200*a)
    #Création du M puis de A pour former le logo MA
    M(a)
    A(a)
    #Création du Présente sur un cadre noir avec la fonction "presente"
    presente(a)
    #Préparation à l'écriture de "FA" à côté du logo "MA"
    color("black")
    forward(520*a)
    #Ecriture de "FA". "a/2" indique la taille, "0" indique que seulement "FA"
    #doit-être écrit.
    SIGNATURE(a/2,0)
    #La ligne de commande "time.sleep(temps)" sert à faire un temps d'attente.
    #Je ne voulais pas que la création du bâteau s'enchène juste après le logo.
    #La suite s'exécutera dans 2 secondes.
    time.sleep(2)
    #"""
    #Préparation à la création du bâteau
    reset()
    speed(8)
    #Création du bâteau
    bateau(a)
    #
    #Mise en place pour faire en plus petit un logo "MA"
    lt(45)
    up()
    backward(1200*a)
    rt(90)
    forward(130*a)
    lt(90)
    #Création du logo "MA"
    M(a/3)
    A(a/3)
    #Fin de la création du bâteau.

    #Préparation à la création du cadre
    speed(8)
    #backward() → sert à placer le curseur sur le bord du bâteau au lieu de le
    #laisser sur le bord du logo "MA".
    backward(215*a)
    setheading(0)
    up()
    #backward() → distance qui sépare le bord droit du bâteau avec le côté

    #Je créer une variable Lcadre pour réutiliser plus facilement cette longueur
    #plus loin dans le code.
    #Le "((cos(radians(45))*(220*a))*2+(308*a+800*a))" correspond à la longueur
    #du bateau. Le "50*a" correspond à la distance entre le côté gauche du cadre
    #au côté gauche du bâteau (et c'est la même chose pour la droite, donc fois
    #2)
    #Ainsi, "Lcadre" est la longueur de mon cadre.
    Lcadre=((cos(radians(45))*(220*a))*2+(308*a+800*a))+(0)*2 ###2500

    #La variable "dCBord" est la longueur séparant le côté gauche du cadre, au
    #côté gauche du bâteau (cette longueur sert à éviter que le cadre colle le
    #bord des bâteaux.
    #Cette variable me permettra de différencier la longueur Lcadre (qui est au
    #final la même longueur du bâteau) et la longueur séparant le bord du
    #bâteau au cadre.

    #"Lcadre/6" est la taille séparant un côté au côté du cadre.
    #si je veux prendre en compte les deux côté, il faut que je multiplie
    #"dCBord" par 2.
    dCBord=Lcadre/6
    backward((dCBord)+0)
    down()
    #Création d'un morceau du cadre (un peu du côté gauche + haut).
    color("black")
    lt(90)
    forward(1000*a)
    rt(90)

    forward(Lcadre+dCBord*2)
    #Création d'un autre morceau du cadre du côté droit.
    ####begin_fill()
    rt(90)
    forward(200*a)
    #Création d'un soleil
    begin_fill()
    color("yellow")
    rt(90)
    #Fonction créant un petit morceau du soleil plus un rayon.
    def morceausoleil(a):
        #Création d'un morceau de cercle
        circle(-(120*a),30)
        #Création d'un rayon
        rt(90)
        backward(150*a)
        forward(150*a)
        lt(90)
    #Il va faire 3 morceau de soleil en appellant 3 fois la fonction
    #morceausoleil.
    for i in range(3):
        morceausoleil(a)
    #Création de la fin du soleil
    circle(-(160*a),30)
    setheading(0)
    forward(100*a)
    end_fill()
    #Recréation de la parti du cadre qui a été enlevé par le soleil.
    color("black")
    backward(100*a)
    forward(100*a)
    #Création du reste du cadre
    rt(90)
    forward(1000*a)
    forward(150*a)
    rt(90)
    forward(Lcadre+dCBord*2)
    rt(90)
    begin_fill()
    color("blue")
    forward(150*a)
    rt(90)
    #Fonction permettant de créer une vague:
    def vagues(a):
        color("blue")
        down()
        for i in range(9+3):
            circle(102.90*a,50)
            lt(80)
            circle(-102.90*a,-50)
            setheading(0)
    begin_fill()
    #Création des vagues
    vagues(a)
    #Remplissage de couleur bleu pour former l'eau.
    rt(90)
    forward(150*a)
    rt(90)
    forward(Lcadre+dCBord*2)
    end_fill()
    #Recréation des bords du cadre couper par l'eau
    rt(90)
    color("black")
    forward(150*a)
    backward(150*a)
    lt(90)
    backward(Lcadre+dCBord*2)
    lt(90)
    backward(150*a)


    #FIN DU SCRIPT.

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

bonus(0.5)

#-------------------------------------------------------------------------------
