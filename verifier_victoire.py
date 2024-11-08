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