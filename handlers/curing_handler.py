import random
import time
from InquirerPy import inquirer
from utils.clear_terminal import clear_terminal


def handle_curing(creature):
    """
    Gère le processus de guérison d'une créature malade via un mini-jeu de pendu.

    Cette fonction vérifie si la créature est malade, puis propose au joueur
    de participer à un jeu du pendu pour tenter de la guérir. Le succès du
    traitement dépend de la performance au jeu.

    Args:
        creature: L'objet créature à guérir
    """
    clear_terminal()

    # Vérifier si la créature est malade
    if not creature.is_sick:
        print(f"{creature.name} n'est pas malade actuellement.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    # Introduction du mini-jeu
    print(f"Oh non ! {creature.name} est malade et a besoin d'un remède.")
    print("Vous avez rencontré le pharmacien du village.")
    print("Il vous propose de jouer au Pendu Médical pour gagner un remède.")
    print("Si vous devinez le mot médical, vous gagnerez le remède parfait pour votre créature.")

    # Proposer de jouer au jeu
    if inquirer.confirm(message="Voulez-vous jouer au Pendu Médical pour guérir votre créature ?").execute():
        result = hangman_game()

        # Traitement du résultat du jeu
        if result:
            # Le joueur a gagné, guérison garantie
            print(f"\nBravo ! Vous avez deviné le mot et gagné le remède parfait !")
            print(f"Vous administrez le remède à {creature.name}...")
            time.sleep(2)
            creature.cure()
            print(f"{creature.name} n'est plus malade !")
        else:
            # Le joueur a perdu, 50% de chance de guérison
            print(f"\nDommage... Le pharmacien vous donne quand même un remède de base.")
            print(f"Ce remède n'est pas aussi efficace, mais il y a une chance qu'il fonctionne.")
            time.sleep(2)
            if random.random() < 0.5:
                creature.cure()
                print(f"Par chance, {creature.name} n'est plus malade !")
            else:
                print(f"Malheureusement, {creature.name} est toujours malade...")
                print("Vous pourrez réessayer plus tard.")
    else:
        print("Vous décidez de ne pas jouer. Le pharmacien s'en va...")

    input("\nAppuyez sur Entrée pour continuer...")


def hangman_game():
    """
    Implémente le mini-jeu du pendu médical.

    Dans ce jeu, le joueur doit deviner un mot lié au domaine médical.
    Il a droit à 6 erreurs avant de perdre.

    Returns:
        bool: True si le joueur a deviné le mot, False sinon
    """
    clear_terminal()
    # Liste de mots médicaux possibles
    medical_words = [
        "aspirine", "vaccin", "remede", "docteur", "infirmier",
        "pharmacie", "ordonnance", "fievre", "antibiotique", "virus",
        "medicament", "seringue", "vitamine", "guerison", "bandage",
        "sirop", "comprime", "traitement", "hopital", "sante"
    ]

    # Sélection aléatoire d'un mot et initialisation de l'affichage
    word = random.choice(medical_words)
    word_display = ["_" for _ in word]

    # Configuration des erreurs
    max_errors = 6
    errors = 0

    # Suivi des lettres déjà proposées
    guessed_letters = []

    # Boucle principale du jeu
    while errors < max_errors and "_" in word_display:
        clear_terminal()
        print("=== JEU DU PENDU MÉDICAL ===")

        display_hangman(errors)

        print("\nMot à deviner : " + " ".join(word_display))

        # Afficher les lettres déjà essayées
        if guessed_letters:
            print("Lettres déjà essayées : " + ", ".join(sorted(guessed_letters)))

        print(f"Tentatives restantes : {max_errors - errors}")

        # Demander une lettre au joueur
        letter = inquirer.text(
            message="Proposez une lettre :",
            validate=lambda x: len(x) == 1 and x.isalpha() and x.lower() not in guessed_letters,
            invalid_message="Veuillez entrer une seule lettre non encore essayée."
        ).execute().lower()

        guessed_letters.append(letter)

        # Vérifier si la lettre est dans le mot
        if letter in word:
            print(f"Bien joué ! La lettre '{letter}' est dans le mot.")
            for i in range(len(word)):
                if word[i] == letter:
                    word_display[i] = letter
            time.sleep(1)
        else:
            print(f"Dommage, la lettre '{letter}' n'est pas dans le mot.")
            errors += 1
            time.sleep(1)

    # Affichage du résultat final
    clear_terminal()
    print("=== JEU DU PENDU MÉDICAL ===")
    display_hangman(errors)
    print("\nMot à deviner : " + " ".join(word_display))

    # Déterminer si le joueur a gagné ou perdu
    if "_" not in word_display:
        print(f"\nBravo ! Vous avez deviné le mot : {word}")
        return True
    else:
        print(f"\nPerdu ! Le mot était : {word}")
        return False


def display_hangman(errors):
    """
    Affiche le dessin du pendu correspondant au nombre d'erreurs.

    Args:
        errors (int): Le nombre d'erreurs commises (0-6)
    """
    stages = [
        # État initial (0 erreur)
        """





        =========
        """,
        # 1 erreur
        """
           |
           |
           |
           |
           |
        =========
        """,
        # 2 erreurs
        """
           +---+
           |
           |
           |
           |
        =========
        """,
        # 3 erreurs
        """
           +---+
           |   |
           |
           |
           |
        =========
        """,
        # 4 erreurs
        """
           +---+
           |   |
           |   O
           |
           |
        =========
        """,
        # 5 erreurs
        """
           +---+
           |   |
           |   O
           |  /|\\
           |
        =========
        """,
        # 6 erreurs (pendu complet)
        """
           +---+
           |   |
           |   O
           |  /|\\
           |  / \\
        =========
        """
    ]
    print(stages[errors])