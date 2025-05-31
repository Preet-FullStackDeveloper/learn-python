"""
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
"""
import random

number = random.randint(1, 100)
print(f'Number = {number}')
input_number = -1

while input_number != number:
    input_number = int(input("Guess a number between 1 and 100: "))
    if input_number < number:
        print("Higher number please")
    elif input_number > number:
        print("Lower number please")

print(f"Congratulations! You've guessed the number {number} correctly.")
