'''
1 for stone
0 for paper
-1 for scissors
'''

import random
computer = random.choice([1, 0, -1])  # Randomly choose between stone, paper, or scissors
player = int(input("Enter your choice (1 for stone, 0 for paper, -1 for scissors): "))

dict = {
    1: "stone",
    0: "paper",
    -1: "scissors"
}

print(f"Computer chose: {dict[computer]}")
print(f"You chose: {dict[player]}")

if (player == computer):
    print("It's a tie!")
elif (player == 1 and computer == -1) or (player == 0 and computer == 1) or (player == -1 and computer == 0):
    print("You win!")
else:
    print("You lose!")