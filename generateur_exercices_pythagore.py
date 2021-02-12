from math import sqrt
from random import randint


def generer():
    go = 1
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    Aa = randint(0, 25)
    A = alphabet.pop(Aa)
    Bb = randint(0, 24)
    B = alphabet.pop(Bb)
    Cc = randint(0, 23)
    C = alphabet.pop(Cc)

    theoreme_ou_reciproque = randint(1, 2)
    un_ou_deux = randint(1, 2)

    if theoreme_ou_reciproque == 1:

        if un_ou_deux == 1 :
            côté_1 = randint(1, 50)
            côté_2 = randint(1, 50)
            hypoténuse = 0
            print("On a {}{}{} un triangle rectangle en {}, avec {}{} = {} et {}{} = {}.".format(A, B, C, A, A, B, côté_1, A, C, côté_2))
            print("Calculer {}{}.".format(B, C))

        if un_ou_deux == 2 :
            hypoténuse = randint(1, 80)
            côté_1 = randint(1, 50)
            côté_2 = 0
            print("On a {}{}{} un triangle rectangle en {}, avec {}{} = {} et {}{} = {}.".format(A, B, C, A, B, C, hypoténuse, A, B, côté_1))
            print("Calculer {}{}.".format(A, C))

    if theoreme_ou_reciproque == 2 :

        if un_ou_deux == 1 :
            hypoténuse = randint(1, 80)
            côté_1 = randint(1, 50)
            côté_2 = randint(1, 50)
            print("On a {}{}{} un triangle avec {}{} = {}, {}{} = {} et {}{} = {}.".format(A, B, C, A, B, côté_1, A, C, côté_2, B, C, hypoténuse))
            print("Ce triangle est-il rectangle ?")
            
        if un_ou_deux == 2 :
            n = randint(1, 6)
            p = randint(1, 6)
            côté_2 = n*n - p*p
            côté_1 = 2*n*p
            hypoténuse = n*n + p*p

            print("On a {}{}{} un triangle avec {}{} = {}, {}{} = {} et {}{} = {}.".format(A, B, C, A, B, côté_1, A, C, côté_2, B, C, hypoténuse))
            print("Ce triangle est-il rectangle ?")
    return (côté_1 , côté_2 , hypoténuse)
            
def corriger(côté_1 , côté_2 , hypoténuse):
    if hypoténuse == 0:

        print(" On sait que le triangle {}{}{} est rectangle en {}. ".format(A, B, C, A))
        print(" D'après Pythagore, on a : ")
        print(" {}{}^2 = {}{}^2 + {}{}^2".format(B, C, A, B, A, C))
        print(" Ainsi, {}{}^2 = {}^2 + {}^2 ".format(B, C, côté_1, côté_2))
        print(" d'où : {}{}^2 = {} + {} ".format(B, C, (côté_1 ** 2), (côté_2 ** 2)))
        print(" {}{}^2 = {} ".format(B, C, (côté_1 ** 2) + (côté_2 ** 2)))
        print(" {}{} = sqrt({})     (car une longueur est toujours positive) ".format(B, C, abs((côté_1 ** 2) + (côté_2 ** 2))))
        print(" Donc  {}{} = {} ".format(B, C, sqrt(abs((côté_1 ** 2) + (côté_2 ** 2)))))

    elif côté_1 == 0:

        print(" On sait que le triangle {}{}{} est rectangle en {}. ".format(A, B, C, A))
        print(" D'après Pythagore, on a : ")
        print(" {}{}^2 = {}{}^2 + {}{}^2".format(B, C, A, B, A, C))
        print(" Ainsi, {}{}^2 = {}{}^2 - {}{}^2 ".format(A, B, B, C, A, C))
        print(" {}{}^2 = {}^2 - {}^2 ".format(A, B, hypoténuse, côté_2))
        print(" d'où : {}{}^2 = {} - {} ".format(A, B, (hypoténuse ** 2), (côté_2 ** 2)))
        print(" {}{}^2 = {} ".format(A, B, (hypoténuse ** 2) - (côté_2 ** 2)))
        print(" {}{} = sqrt({})     (car une longueur est toujours positive) ".format(A, B, abs((hypoténuse ** 2) - (côté_2 ** 2))))
        print(" Donc  {}{} = {} ".format(A, B, sqrt(abs((hypoténuse ** 2) - (côté_2 ** 2)))))


    elif côté_2 == 0:

        print(" On sait que le triangle {}{}{} est rectangle en {}. ".format(A, B, C, A))
        print(" D'après Pythagore, on a : ")
        print(" {}{}^2 = {}{}^2 + {}{}^2".format(B, C, A, B, A, C))
        print(" Ainsi, {}{}^2 = {}{}^2 - {}{}^2 ".format(A, C, B, C, A, B))
        print(" {}{}^2 = {}^2 - {}^2 ".format(A, C, hypoténuse, côté_1))
        print(" d'où : {}{}^2 = {} - {} ".format(A, C, (hypoténuse ** 2), (côté_1 ** 2)))
        print(" {}{}^2 = {} ".format(A, C, (hypoténuse ** 2) - (côté_1 ** 2)))
        print(" {}{} = sqrt({})     (car une longueur est toujours positive) ".format(A, C, abs((hypoténuse ** 2) - (côté_1 ** 2))))
        print(" Donc  {}{} = {} ".format(A, C, sqrt(abs((hypoténuse ** 2) - (côté_1 ** 2)))))

    else:
        a = hypoténuse ** 2
        b = côté_1 ** 2
        c = côté_2 ** 2

        print(" On a {}{} le côté le plus grand.".format(B, C))
        print(" On calcule séparément : ")
        print(" {}{}^2 = {}^2 = {}   et  {}{}^2 + {}{}^2 = {}^2 + {}^2 = {} + {} = {} ".format(B, C, hypoténuse, (hypoténuse ** 2), A, B, A, C, côté_1, côté_2, (côté_1 ** 2), (côté_2 ** 2), ((côté_1 ** 2) + (côté_2 ** 2))))

        if a - (b + c) == 0:
            print(" Donc {}{}^2 = {}{}^2 + {}{}^2 ".format(B, C, A, B, A, C))
            print(" Donc, d'après la réciproque du théorème de Pythagore, le triangle {}{}{} est rectangle en {}. ".format(A, B, C, A))

        elif a != (b + c):
            print(" Donc {}{}^2 != {}{}^2 + {}{}^2 ".format(B, C, A, B, A, C))
            print(" Donc, d'après la réciproque du théorème de Pythagore, le triangle {}{}{} n'est pas rectangle. ".format(A, B, C))
