







# Tour du joueur humain
def tour_joueur(grille, joueur):
    position = int(input(f"Joueur {joueur}, choisissez une case (1-9): ")) - 1
    if grille[position] == " ":
        grille[position] = joueur