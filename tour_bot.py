import random

# Tour du bot
def tour_bot(grille):
    position = random.randint(0, 8)
    while grille[position] != " ":
        position = random.randint(0, 8)
    grille[position] = "O"
    print("Le bot a joué.")
  