def game_controller(creature):
    print(f"Voici {creature.name} :")
    start_line = None
    end_line = None
    match creature.__class__.__name__:
        case "Puppy":
            start_line = 3
            end_line = 12
        case "Kitten":
            start_line = 16
            end_line = 21
        case "Dragon":
            start_line = 25
            end_line = 35
        case "Bunny":
            start_line = 39
            end_line = 53
        case "Hamster":
            start_line = 57
            end_line = 71
        case "FoxCub":
            start_line = 75
            end_line = 89
        case "Penguin":
            start_line = 93
            end_line = 110
        case "Panda":
            start_line = 114
            end_line = 130
        case "BabyTurtle":
            start_line = 134
            end_line = 157

    with open("utils/ascii_art.txt", "r") as file:
        lines = file.readlines()
        for line in lines[start_line:end_line]:
            print(line, end="")

