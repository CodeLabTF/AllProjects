

import random 

secretNumber = random.randint(1, 30)

for guessTaken in range (1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is to low")
    elif guess > secretNumber:
        print("Your guess is to high")
    else:
        break # --> This condition is the right guess!

if guess == secretNumber:
    print("You guessed my number in " + str(guessTaken) + " guesses!")
else: 
    print("Nope. The number I was thinking of was. " + str(secretNumber))


