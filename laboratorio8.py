import random
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Adivine un numero entre 1 y 10: ")
    if int(guess) == number:
        print("Adivinastes {}. That is correct! Ganastes!".format(guess))
        isGuessRight = True
    else:
        print("Tu numero elegido fue: {}. Lo siento, Ese no fue. Prueba de nuevo.".format(guess))
