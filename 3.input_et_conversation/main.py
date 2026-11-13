age = input("Quel est votre age ? ") # instruction qui permet de demander à l'utilisateur de saisir une valeur et de la stocker dans une variable
is_adult = int(age) >= 18 # instruction qui permet d'effectuer une comparaison entre une variable et un nombre et de stocker le resultat dans une variable

if is_adult: # instruction qui permet de verifier si une condition est vraie
    print("Vous etes majeur "  + age) # instruction qui permet d'affiche un texte en parametre
else: # instruction qui permet de verifier si une condition est fausse
    print("Vous etes mineur " + age) # instruction qui permet d'affiche un texte en parametre
