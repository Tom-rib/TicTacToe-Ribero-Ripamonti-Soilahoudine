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



