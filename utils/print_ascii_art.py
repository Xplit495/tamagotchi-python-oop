def print_ascii_art(creature):
    """
    Affiche l'art ASCII correspondant à la créature spécifique.

    Cette fonction lit un fichier ASCII art prédéfini et affiche
    l'illustration correspondant au type de créature.

    Args:
        creature (Creature): L'objet créature dont on souhaite afficher l'art ASCII.

    Fonctionnement :
    - Détermine la plage de lignes dans le fichier ASCII art
      en fonction du type de créature
    - Imprime le nom de la créature
    - Lit et affiche les lignes correspondantes du fichier ASCII art

    Note:
    - Nécessite un fichier 'ascii_art.txt' avec des sections prédéfinies
    - Chaque type de créature a une section spécifique dans le fichier
    """
    # Affiche le nom de la créature
    print(f"{creature.name} :")

    # Variables pour stocker les numéros de ligne de début et de fin
    start_line = None
    end_line = None

    # Sélection de la section ASCII art en fonction du type de créature
    match creature.__class__.__name__:
        case "Puppy":
            start_line = 2
            end_line = 13
        case "Kitten":
            start_line = 15
            end_line = 22
        case "Dragon":
            start_line = 24
            end_line = 36
        case "Bunny":
            start_line = 38
            end_line = 54
        case "Hamster":
            start_line = 56
            end_line = 72
        case "FoxCub":
            start_line = 74
            end_line = 90
        case "Penguin":
            start_line = 92
            end_line = 111
        case "Panda":
            start_line = 113
            end_line = 131
        case "BabyTurtle":
            start_line = 133
            end_line = 158

    # Lecture et affichage de la section ASCII art correspondante
    with open("ascii_art.txt", "r") as file:
        # Lit toutes les lignes du fichier
        lines = file.readlines()
        # Affiche uniquement les lignes correspondant à la créature
        for line in lines[start_line:end_line]:
            print(line, end="")