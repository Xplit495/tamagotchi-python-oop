import random
import time
from InquirerPy import inquirer
from utils.clear_terminal import clear_terminal


def handle_curing(creature):
    clear_terminal()

    if not creature.is_sick:
        print(f"{creature.name} n'est pas malade actuellement.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"Oh non ! {creature.name} est malade et a besoin d'un remède.")
    print("Vous avez rencontré le pharmacien du village.")
    print("Il vous propose de jouer au Pendu Médical pour gagner un remède.")
    print("Si vous devinez le mot médical, vous gagnerez le remède parfait pour votre créature.")

    if inquirer.confirm(message="Voulez-vous jouer au Pendu Médical pour guérir votre créature ?").execute():
        result = hangman_game()

        if result:
            print(f"\nBravo ! Vous avez deviné le mot et gagné le remède parfait !")
            print(f"Vous administrez le remède à {creature.name}...")
            time.sleep(2)
            creature.cure()
            print(f"{creature.name} n'est plus malade !")
        else:
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
    clear_terminal()
    medical_words = [
        "aspirine", "vaccin", "remede", "docteur", "infirmier",
        "pharmacie", "ordonnance", "fievre", "antibiotique", "virus",
        "medicament", "seringue", "vitamine", "guerison", "bandage",
        "sirop", "comprime", "traitement", "hopital", "sante"
    ]

    word = random.choice(medical_words)
    word_display = ["_" for _ in word]

    max_errors = 6
    errors = 0

    guessed_letters = []

    while errors < max_errors and "_" in word_display:
        clear_terminal()
        print("=== JEU DU PENDU MÉDICAL ===")

        display_hangman(errors)

        print("\nMot à deviner : " + " ".join(word_display))

        if guessed_letters:
            print("Lettres déjà essayées : " + ", ".join(sorted(guessed_letters)))

        print(f"Tentatives restantes : {max_errors - errors}")

        letter = inquirer.text(
            message="Proposez une lettre :",
            validate=lambda x: len(x) == 1 and x.isalpha() and x.lower() not in guessed_letters,
            invalid_message="Veuillez entrer une seule lettre non encore essayée."
        ).execute().lower()

        guessed_letters.append(letter)

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

    clear_terminal()
    print("=== JEU DU PENDU MÉDICAL ===")
    display_hangman(errors)
    print("\nMot à deviner : " + " ".join(word_display))

    if "_" not in word_display:
        print(f"\nBravo ! Vous avez deviné le mot : {word}")
        return True
    else:
        print(f"\nPerdu ! Le mot était : {word}")
        return False


def display_hangman(errors):
    """Affiche le dessin du pendu selon le nombre d'erreurs"""
    stages = [
        """





        =========
        """,
        """
           |
           |
           |
           |
           |
        =========
        """,
        """
           +---+
           |
           |
           |
           |
        =========
        """,
        """
           +---+
           |   |
           |
           |
           |
        =========
        """,
        """
           +---+
           |   |
           |   O
           |
           |
        =========
        """,
        """
           +---+
           |   |
           |   O
           |  /|\\
           |
        =========
        """,
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