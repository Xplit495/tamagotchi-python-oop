import time

from utils.clear_terminal import clear_terminal
import random
import keyboard


def handle_playing(creature):
    clear_terminal()

    if creature.energy < 10:
        print(f"{creature.name} est trop fatigué pour jouer maintenant.")
        input("Appuyez sur Entrée pour continuer...")
        return

    mini_game(creature)


def mini_game(creature):
    print(f"Vous allez jouer à un mini-jeu pour augmenter le bonheur de {creature.name} !\n")
    print(f"Vous allez incarner {creature.name} et vous allez devoir vous retrouver dans la carte.")
    print("Bien sur votre position est aléatoire (ce serait trop facile sinon).\n")

    hide_and_seek_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    random_position = get_random_position()
    user_position = (4, 4)

    counter = 0

    while True:
        print_map(hide_and_seek_map)

        print('\n\nVotre position actuelle est représenté par 📍, vous pouvez maintenant utiliser les flèches directionnelles pour vous déplacer.\n')
        time.sleep(0.5)

        direction = get_user_input()

        user_position_saved = user_position

        match direction:
            case 'up':
                if user_position[0] > 0:
                    user_position = (user_position[0] - 1, user_position[1])
                else:
                    print("Vous ne pouvez pas aller plus haut.")
                    time.sleep(1)
            case 'down':
                if user_position[0] < 8:
                    user_position = (user_position[0] + 1, user_position[1])
                else:
                    print("Vous ne pouvez pas aller plus bas.")
                    time.sleep(1)
            case 'left':
                if user_position[1] > 0:
                    user_position = (user_position[0], user_position[1] - 1)
                else:
                    print("Vous ne pouvez pas aller plus à gauche.")
                    time.sleep(1)
            case 'right':
                if user_position[1] < 8:
                    user_position = (user_position[0], user_position[1] + 1)
                else:
                    print("Vous ne pouvez pas aller plus à droite.")
                    time.sleep(1)

        if user_position == random_position:
            print("Bravo, vous vous êtes retrouvé !")
            creature.play(counter, counter/2)
            time.sleep(5)
            break

        counter += 1

        hide_and_seek_map[user_position_saved[0]][user_position_saved[1]] = 2
        hide_and_seek_map[user_position[0]][user_position[1]] = 1
        clear_terminal()


def get_user_input():
    while True:
        if keyboard.is_pressed('up'):
            return 'up'
        elif keyboard.is_pressed('down'):
            return 'down'
        elif keyboard.is_pressed('left'):
            return 'left'
        elif keyboard.is_pressed('right'):
            return 'right'

def get_random_position():
    while True:
        random_position = (random.randint(0, 8), random.randint(0, 8))
        if random_position[0] != 4 or random_position[1] != 4:
            return random_position


def print_map(hide_and_seek_map):
    for line in range (len(hide_and_seek_map)):
        print('\n', end='')
        for column in range (len(hide_and_seek_map[line])):
            if hide_and_seek_map[line][column] == 0:
                print('🪨', end=' ')
            elif hide_and_seek_map[line][column] == 1:
                print('📍', end=' ')
            elif hide_and_seek_map[line][column] == 2:
                print('❌ ', end=' ')
