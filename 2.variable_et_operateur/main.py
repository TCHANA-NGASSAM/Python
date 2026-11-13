my_age = 13 # instruction qui permet de stocker une valeur dans une variable
print(type(my_age)) # instruction qui permet d'affiche le type de la variable
print(my_age) # instruction qui permet d'affiche un texte en parametre
my_variable_type = type(my_age) # instruction qui permet d'affiche le type de la variable
print(my_variable_type)

"""
il est a note que python est un langage de programmation qui est fortement typé,
c'est a dire que chaque variable a un type bien defini et ne peut pas changer de type au cours de l'execution du programme.

nous avons les differents types de variables en python:
- int: entier
- float: nombre à virgule flottante
- str: chaîne de caractères
- bool: valeur booléenne

"""

my_name = "Adrien" # instruction qui permet de stocker une valeur dans une variable
my_description = 'je suis un developpeur python' # instruction qui permet de stocker une valeur dans une variable
print(my_name) # instruction qui permet d'affiche un texte en parametre
print(my_description) # instruction qui permet d'affiche un texte en parametre


num1 = 10 # instruction qui permet de stocker une valeur dans une variable
num2 = 444# instruction qui permet de stocker une valeur dans une variable
sum = num1 + num2    # instruction qui permet d'effectuer une addition entre deux variables et de stocker le resultat dans une variable
print(sum) # instruction qui permet d'affiche un texte en parametre


str1 = "Bonjour" # instruction qui permet de stocker une valeur dans une variable
str2 = "le monde" # instruction qui permet de stocker une valeur dans une variable

concatenation = str1 + " " + str2    # instruction qui permet de concaténer deux chaînes de caractères et de stocker le resultat dans une variable
print(concatenation) # instruction qui permet d'affiche un texte en parametre

"""

il nest pas possible de concaténer une chaîne de caractères avec un nombre entier ou un nombre à virgule flottante,
il est donc nécessaire de convertir le nombre en chaîne de caractères avant de pouvoir le concaténer

"""

sum2 = str(num1) + " " + str(num2)    # instruction qui permet de convertir un nombre entier et un nombre à virgule flottante en chaîne de caractères et de les concaténer
print(sum2) # instruction qui permet d'affiche un texte en parametre
subnum = num1 - num2    # instruction qui permet d'effectuer une soustraction entre deux variables et de stocker le resultat dans une variable
print(subnum) # instruction qui permet d'affiche un texte en parametre

mult = num1 * num2    # instruction qui permet d'effectuer une multiplication entre deux variables et de stocker le resultat dans une variable
print(mult) # instruction qui permet d'affiche un texte en parametre    

div = num1 / num2    # instruction qui permet d'effectuer une division entre deux variables et de stocker le resultat dans une variable
print(div) # instruction qui permet d'affiche un texte en parametre


"""
il est a noter que la division entre deux nombres entiers retourne un nombre à virgule flottante,
il est donc nécessaire de convertir le resultat en entier si l'on souhaite obtenir un nombre entier    

"""

comparaison = num1 > num2    # instruction qui permet d'effectuer une comparaison entre deux variables et de stocker le resultat dans une variable
print(comparaison) # instruction qui permet d'affiche un texte en parametre


"""
il est a noter que la comparaison entre deux nombres entiers retourne une valeur booléenne,
il est donc nécessaire de convertir le resultat en entier si l'on souhaite obtenir un nombre entier
les operateurs de comparaison sont les suivants:

- ==: egal a
- !=: different de
- <: inferieur a
- >: superieur a
- <=: inferieur ou egal a
- >=: superieur ou egal a

"""


"""
les operateurs logiques sont les suivants:

- and: et
- or: ou
- not: non

"""

is_adult = True # instruction qui permet de stocker une valeur dans une variable
is_male = False # instruction qui permet de stocker une valeur dans une variable

is_adult_and_male = is_adult and is_male
print(is_adult_and_male) # instruction qui permet d'affiche un texte en parametre

is_not_male = not is_male # instruction qui permet d'effectuer une negation sur une variable et de stocker le resultat dans une variable
print(is_not_male) # instruction qui permet d'affiche un texte en parametre


"""
la precedence des operateurs logiques est la suivante:
- not
- and
- or
les operateurs logiques peuvent etre combiner entre eux pour former des expressions logiques plus complexes:
exemple: (is_adult and is_male) or (not is_male)
"""
