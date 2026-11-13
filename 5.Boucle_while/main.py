import random

number_to_guess = random.randint(1, 1000)
guess = 0
while guess != number_to_guess:
    saisie = input("Devinez le nombre entre 1 et 1000 : ")
    
    try:
        guess = int(saisie)
    except ValueError:
        print("Veuillez entrer un nombre valide. entier pas de lettres ou de caractères spéciaux.")
        continue
    
    if guess < 1 or guess > 1000:
        print("Veuillez entrer un nombre entre 1 et 1000.")
        continue

    if guess < number_to_guess:
        print("Le nombre à deviner est plus grand que", guess)
    elif guess > number_to_guess:
        print("Le nombre à deviner est plus petit que", guess)
    else:
        print("Félicitations ! Vous avez deviné le nombre", number_to_guess)
        