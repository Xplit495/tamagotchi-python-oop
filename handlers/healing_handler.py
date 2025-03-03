import time
import random
from InquirerPy import inquirer
from utils.clear_terminal import clear_terminal


def handle_healing(creature):
    """
    Gère le processus de guérison de la créature via un mini-jeu de morpion.

    Cette fonction vérifie si la créature a besoin de soins, puis propose au joueur
    de participer à un jeu de morpion contre Dr. Guérisou pour obtenir un spray médicinal.
    L'efficacité du spray dépend du résultat de la partie.

    Args:
        creature: L'objet créature à soigner
    """
    clear_terminal()

    # Vérifier si la créature a besoin de soins
    if creature.health == creature.max_health:
        print(f"{creature.name} est déjà en parfaite santé !")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    # Introduction du mini-jeu
    print(f"Vous avez rencontré le Dr. Guérisou qui a un spray médicinal !")
    print(f"Il propose de soigner {creature.name}, mais il veut vous défier dans une partie de morpion d'abord.")
    print("Si vous gagnez, il vous donnera le spray gratuitement.")
    print("Si vous perdez ou faites match nul, ce sera quand même gratuit mais ce sera moins efficace.")

    # Proposer de jouer au jeu
    if inquirer.confirm(message="\nVoulez-vous jouer au morpion contre le Dr. Guérisou ?").execute():
        result = tic_tac_toe()

        # Traitement du résultat selon l'issue de la partie
        if result == "win":
            # Victoire: 50% de la santé max est restaurée
            healing_amount = int(creature.max_health * 0.5)
            print(f"\nVous avez gagné ! Le Dr. Guérisou vous donne le spray premium.")
            print(f"Vous soignez {creature.name} avec le spray...")
            time.sleep(2)
            old_health = creature.health
            creature.heal(healing_amount)
            print(f"{creature.name} a récupéré {creature.health - old_health} points de santé !")
        elif result == "draw":
            # Match nul: 25% de la santé max est restaurée
            healing_amount = int(creature.max_health * 0.25)
            print(f"\nMatch nul ! Le Dr. Guérisou vous vend un spray basique.")
            print(f"Vous soignez {creature.name} avec le spray...")
            time.sleep(2)
            old_health = creature.health
            creature.heal(healing_amount)
            print(f"{creature.name} a récupéré {creature.health - old_health} points de santé !")
        else:
            # Défaite: 10% de la santé max est restaurée
            healing_amount = int(creature.max_health * 0.1)
            print(f"\nVous avez perdu ! Le Dr. Guérisou vous vend un spray de mauvaise qualité.")
            print(f"Vous soignez {creature.name} avec le spray...")
            time.sleep(2)
            old_health = creature.health
            creature.heal(healing_amount)
            print(f"{creature.name} a récupéré {creature.health - old_health} points de santé !")
    else:
        print("Vous décidez de ne pas jouer. Le Dr. Guérisou s'en va...")

    input("\nAppuyez sur Entrée pour continuer...")


def tic_tac_toe():
    """
    Implémente le mini-jeu de morpion contre l'IA.

    Le joueur est X, l'ordinateur est O. Un joueur est choisi aléatoirement pour commencer.

    Returns:
        str: "win" si le joueur gagne, "lose" s'il perd, "draw" en cas de match nul
    """
    clear_terminal()
    print("=== Jeu de Morpion contre le Dr. Guérisou ===")
    print("Vous êtes X, le Dr. Guérisou est O")
    print("Pour jouer, entrez le numéro de la case (1-9) comme indiqué ci-dessous :")
    print_numbered_board()

    # Initialisation du plateau (vide)
    board = [" " for _ in range(9)]

    # Choix aléatoire du premier joueur
    current_player = random.choice(["X", "O"])
    if current_player == "O":
        print("\nLe Dr. Guérisou commence !")
    else:
        print("\nVous commencez !")

    input("\nAppuyez sur Entrée pour commencer...")
    clear_terminal()

    # Boucle principale du jeu
    while True:
        if current_player == "X":  # Tour du joueur
            print_board(board)

            # Afficher les positions valides
            valid_positions = [i + 1 for i, val in enumerate(board) if val == " "]
            position_str = ", ".join(map(str, valid_positions))

            print(f"Cases disponibles : {position_str}")

            # Demander au joueur de choisir une case
            while True:
                try:
                    move = inquirer.text(
                        message="Entrez le numéro de la case :",
                        validate=lambda x: x.isdigit() and 1 <= int(x) <= 9 and board[int(x) - 1] == " ",
                        invalid_message="Case déjà occupée ou invalide ! Choisissez une autre case."
                    ).execute()

                    # Convertir l'entrée en indice de tableau (0-8)
                    move = int(move) - 1
                    board[move] = "X"
                    break
                except ValueError:
                    print("Veuillez entrer un nombre entre 1 et 9.")
        else:  # Tour de l'IA
            print("\nLe Dr. Guérisou réfléchit...")
            time.sleep(random.uniform(0.5, 1.5))  # Pause aléatoire pour simuler la réflexion
            move = get_ai_move(board)
            board[move] = "O"
            print(f"Le Dr. Guérisou joue en case {move + 1}")

        # Vérifier si le joueur actuel a gagné
        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                print("\nVous avez gagné !")
                return "win"
            else:
                print("\nLe Dr. Guérisou a gagné !")
                return "lose"

        # Vérifier s'il y a match nul
        if " " not in board:
            print_board(board)
            print("\nMatch nul !")
            return "draw"

        # Changer de joueur
        current_player = "O" if current_player == "X" else "X"
        clear_terminal()
        print("=== Jeu de Morpion contre le Dr. Guérisou ===")
        print("Vous êtes X, le Dr. Guérisou est O")


def print_numbered_board():
    """
    Affiche un plateau de morpion numéroté pour indiquer les positions.
    """
    print("\n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\n")


def print_board(board):
    """
    Affiche l'état actuel du plateau de morpion.

    Args:
        board (list): Liste représentant l'état du plateau
    """
    print("\n")
    symbols = []
    for cell in board:
        if cell == "X":
            symbols.append("X")
        elif cell == "O":
            symbols.append("O")
        else:
            symbols.append(" ")

    print(f" {symbols[0]} | {symbols[1]} | {symbols[2]} ")
    print("---+---+---")
    print(f" {symbols[3]} | {symbols[4]} | {symbols[5]} ")
    print("---+---+---")
    print(f" {symbols[6]} | {symbols[7]} | {symbols[8]} ")
    print("\n")


def check_winner(board, player):
    """
    Vérifie si le joueur spécifié a gagné.

    Args:
        board (list): État actuel du plateau
        player (str): Joueur à vérifier ("X" ou "O")

    Returns:
        bool: True si le joueur a gagné, False sinon
    """
    # Vérifier les lignes horizontales
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Vérifier les lignes verticales
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Vérifier les diagonales
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False


def get_ai_move(board):
    """
    Détermine le meilleur coup pour l'IA selon une stratégie simple.

    Stratégie:
    1. Gagner si possible
    2. Bloquer le joueur s'il peut gagner
    3. Prendre le centre s'il est libre
    4. Prendre un coin s'il est libre
    5. Prendre n'importe quelle case disponible

    Args:
        board (list): État actuel du plateau

    Returns:
        int: Indice de la case choisie (0-8)
    """
    # 1. Vérifier si l'IA peut gagner au prochain coup
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                board[i] = " "
                return i
            board[i] = " "

    # 2. Vérifier si le joueur peut gagner au prochain coup et le bloquer
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = " "
                return i
            board[i] = " "

    # 3. Prendre le centre s'il est disponible
    if board[4] == " ":
        return 4

    # 4. Prendre un coin aléatoire disponible
    corners = [0, 2, 6, 8]
    available_corners = [corner for corner in corners if board[corner] == " "]
    if available_corners:
        return random.choice(available_corners)

    # 5. Prendre une case aléatoire disponible
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)