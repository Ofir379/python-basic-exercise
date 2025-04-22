import random

moves = {
    1: "Jab",
    2: "Cross",
    3: "Hook",
    4: "Uppercut"
}

wins = {
    1: 3,  # Jab > Hook
    2: 1,  # Cross > Jab
    3: 4,  # Hook > Uppercut
    4: 2   # Uppercut > Cross
}

print("Choose your move:")
for num, name in moves.items():
    print(f"{num}: {name}")

try:
    player = int(input("Enter move number: "))
    if player not in moves:
        print("Invalid move.")
        exit()

    opponent = random.randint(1, 4)
    print(f"You chose {moves[player]}, Opponent chose {moves[opponent]}.")

    if player == opponent:
        print("It's a draw!")
    elif wins[player] == opponent:
        print("You win!")
    else:
        print("You lose!")

except ValueError:
    print("Please enter a valid number.")
