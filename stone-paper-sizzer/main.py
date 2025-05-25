import random

computer = random.choice([1, 0, -1]);

player = int(input("Enter 1 for stone, 0 for paper, -1 for scissor: "))

dict = {
    1: "stone",
    0: "paper",
    -1: "scissor"
}

print("Computer chose: " + dict[computer])
print("You chose: " + dict[player])
if computer == player:
    print("It's a tie!")
elif (computer == 1 and player == -1) or (computer == 0 and player == 1) or (computer == -1 and player == 0):
    print("You lose!")
else:
    print("You win!")