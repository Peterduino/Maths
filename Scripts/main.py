import random
from math import sqrt

nv_ex = 1

def calculate_discriminant(a, b, c):
    return (b**2) - (4*a*c)

def calculate_roots(a, b, c):
    disc = calculate_discriminant(a, b, c)
    
    if disc>0:
        x1=(-b-sqrt(disc))/(2*a)
        x2=(-b+sqrt(disc))/(2*a)
        return 2, x1, x2
    elif disc==0:
        x0=(-b)/(2*a)
        return 1, x0, 0
    else:
        return 0, 0, 0

def randint_with_exclude(x : int, y: int, exclude=None):
        if exclude is None:
            exclude = []
        v: int = random.randint(x, y)
        while v in exclude:
            v: int = random.randint(x, y)
        else:
            return v

def generate_quadratic_equation():
    a = randint_with_exclude(-6, 6, [0])
    b = randint_with_exclude(-10, 10)
    c = randint_with_exclude(-6, 6)

    discriminant = calculate_discriminant(a, b, c)

    delta_sign = "<" if discriminant < 0 else ("=" if discriminant == 0 else ">")
    
    if a<0: a_tp=str("-"+str(abs(a)))
    elif a==1: a_tp=""
    else: a_tp=str(a)
    
    if b<0: b_tp=str("- "+str(abs(b)))
    elif b==1: b_tp="+ "
    else: b_tp="+ "+str(b)
    
    if c<0: c_tp=str("- "+str(abs(c)))
    elif c==0: c_tp=""
    else: c_tp="+ "+str(c)

    equation = f"{a_tp}x\u00b2 {b_tp}x {c_tp}" #, Δ {delta_sign} 0

    return equation, discriminant, a, b, c

def print2D():
    equation = generate_quadratic_equation()[0]
    print("Voici une équation du 2nd degré :", equation)

def Exo():
    
    global nv_ex
    
    if nv_ex==1:
        eq = generate_quadratic_equation()
        print("Niveau 1, entre le disciminant du polynome :", eq[0])
        disc = eq[1]
        inp = int(input(": "))
        if disc==inp:
            print("Bonne réponse !")
            nv_ex=2
        else:
            print("Et non ! Δ =", disc)
    elif nv_ex==2:
        eq = generate_quadratic_equation()
        disc = eq[1]
        roots = calculate_roots(eq[2], eq[3], eq[4])
        print(f"Pour le polynome {eq[0]}")
        print("Entre : 'x1 x2' ou 'x0 0', ou '0 0' en fonction des racines existantes")
        rep = input(": ").split()
        
        if rep[0]==roots[1] and rep[1]==roots[2]:
            print("Bonne réponse !")
        elif roots[0]==0:
            print("Et non ! Δ =", disc, "< 0 donc il n'y a aucune racines sur R")
        elif roots[0]==1:
            print("Et non ! Δ =", disc, "= 0 donc la seule racine est ", roots[1])
        elif roots[0]==2:
            print("Et non ! Les racines sont ", roots[1:2])

def help():
    print()
    print("Les commandes disponibles ici sont :")
    print("                                     -> N : générer un Nouveau polynome")
    print("                                     -> E : entrer en mode Exercice")
    print("                                     -> Q : Quitter le mode actuel ou arreter le programme")
    print("                                     -> H : Afficher ces infos")

print2D()
"""print("Pour l'instant, les exos c'est un échec, donc ici tu rafraichis et tu as un nouveau polynome généré aléatoirement")
"""
print()
print("Bienvenu sur l'interface d'exercices sur le 2nd degré")
help()

run = True
while run:
    
    inpt = input(": ")
    
    if inpt=="N" or inpt=="n":
        print2D()
    if inpt=="E" or inpt=="e":
        Exo()
        print("Continuer l'exercices ?('O' oui / 'N' non)")
        again = input(": ")
        while again=="O" or again=="o":
            Exo()
            print("Continuer l'exercices ?('O' oui / 'N' non)")
            input(": ")
        print("Ton niveau a été enregistré, tu reprendra au meme niveau si tu reviens sur Exercice sans fermer cette fenetre")
    if inpt=="Q" or inpt=="q":
        print2D()
    print()
    print("Console générale (N, E, Q, H)")
    
            
