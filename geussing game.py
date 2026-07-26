# Number Guessing Game 
# Created by Zahraa

import random
while True:
    print("Welcome to the Guessing Game!")
    print("Choose difficulty:")
    print("1. Easy (0 - 20)")
    print("2. Medium (0 - 50)")
    print("3. Hard (0 - 100)")

    while True:
        try:
         difficulty = int(input("Enter your choice (1/2/3): "))
         break
        except ValueError:
         print('please enter 1,2 or 3')
    
    low = 0

    if difficulty == 1:
        high = 20
    elif difficulty == 2:
        high = 50
    elif difficulty == 3:
        high = 100
    else:
        print("Invalid choice. Medium mode selected.")
        high = 50

    guesses = 0
    number = random.randint(low, high)

    while True:

        try:
            guess = int(input(f"Input a number between ({low}-{high}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < low or guess > high:
            print("Number out of range!")
            continue

        guesses += 1

        if guess < number:
            print(f"{guess} is too low! Try a higher number ")
        elif guess > number:
            print(f"{guess} is too high! Try a lower number ")
        else:
            print(f"{guess} is correct! Congratulation!")
            break

    print(f"This round took you {guesses} guesses.")
    again = input('play again ? (y/n)').lower()
    if again != 'y':
         print('Thanks for playing !')
         break