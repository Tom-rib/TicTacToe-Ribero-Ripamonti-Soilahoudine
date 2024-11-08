import random

# Fonction pour afficher la grille de jeu
def afficher_grille(grille):
    print(f"{grille[0]} | {grille[1]} | {grille[2]}")
    print("--|---|--")
    print(f"{grille[3]} | {grille[4]} | {grille[5]}")
    print("--|---|--")
    print(f"{grille[6]} | {grille[7]} | {grille[8]}")

# Vérifie si quelqu'un a gagné
def verifier_victoire(grille, joueur):
    # Les combinaisons gagnantes
    if (grille[0] == grille[1] == grille[2] == joueur or  # Ligne du haut
        grille[3] == grille[4] == grille[5] == joueur or  # Ligne du milieu
        grille[6] == grille[7] == grille[8] == joueur or  # Ligne du bas
        grille[0] == grille[3] == grille[6] == joueur or  # Colonne de gauche
        grille[1] == grille[4] == grille[7] == joueur or  # Colonne du milieu
        grille[2] == grille[5] == grille[8] == joueur or  # Colonne de droite
        grille[0] == grille[4] == grille[8] == joueur or  # Diagonale
        grille[2] == grille[4] == grille[6] == joueur):   # Autre diagonale
        return True
    return False

# Tour du joueur humain
def tour_joueur(grille, joueur):
    position = int(input(f"Joueur {joueur}, choisissez une case (1-9): ")) - 1
    if grille[position] == " ":
        grille[position] = joueur

# Tour du bot
def tour_bot(grille):
    position = random.randint(0, 8)
    while grille[position] != " ":
        position = random.randint(0, 8)
    grille[position] = "O"
    print("Le bot a joué.")

# Fonction principale
def jouer():
    # On crée une grille vide
    grille = [" "] * 9
    mode = input("Mode de jeu - 1: Joueur vs Joueur, 2: Joueur vs Bot: ")
    
    joueur_actuel = "X"
    for _ in range(9):  # Limité à 9 tours, maximum pour un tic-tac-toe
        afficher_grille(grille)
        
        # Le tour du joueur ou du bot selon le mode
        if joueur_actuel == "X":
            tour_joueur(grille, "X")
        else:
            if mode == "1":
                tour_joueur(grille, "O")
            else:
                tour_bot(grille)
        
        # Vérification de victoire
        if verifier_victoire(grille, joueur_actuel):
            afficher_grille(grille)
            print(f"Le joueur {joueur_actuel} a gagné!")
            return
        
        # On passe au joueur suivant
        joueur_actuel = "O" if joueur_actuel == "X" else "X"
    
    afficher_grille(grille)
    print("Match nul!")

# Lancer le jeu
jouer()