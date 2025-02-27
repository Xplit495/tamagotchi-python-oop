def game_controller(creature):
    print(f"Voici {creature.name} :")
    start_line = None
    end_line = None
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

    with open("utils/ascii_art.txt", "r") as file:
        lines = file.readlines()
        for line in lines[start_line:end_line]:
            print(line, end="")

