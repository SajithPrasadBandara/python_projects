# Simeple number guessing game

import random

# Set zero to the guessing number 
top_of_rage = input("Enter the number : ")

if top_of_rage.isdigit():
    top_of_rage = int(top_of_rage)

    if top_of_rage <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please enter number next time.")
    quit()

# Guessing number Range
random_number = random.randint(0, top_of_rage)

# How many guessing?
guess = 0

# Random number and user input guessing number check
while True:
    guess += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You were below the number!")

print("You got it in ",guess, " guesses.")