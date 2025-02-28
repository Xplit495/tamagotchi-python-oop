from utils.clear_terminal import clear_terminal

from utils.print_ascii_art import print_ascii_art

def display_creature_status(creature):
    clear_terminal()

    print_ascii_art(creature)

    print(f"========= {creature.name} =========")
    print(f"En vie depuis : {creature.alive_days} jours | Stade: {creature.stage}")
    print("-" * 40)

    stats = [
        {"name": "Santé", "value": creature.health, "max": creature.max_health},
        {"name": "Faim", "value": creature.hunger, "max": creature.max_hunger},
        {"name": "Énergie", "value": creature.energy, "max": creature.max_energy},
        {"name": "Bonheur", "value": creature.happiness, "max": creature.max_happiness}
    ]

    for stat in stats:
        percentage = int((stat["value"] / stat["max"]) * 10)
        bar = "█" * percentage + "░" * (10 - percentage)
        print(f"{stat['name']:8} [{bar}] {stat['value']}/{stat['max']}")

    if creature.is_sick:
        print("\n⚠️  ATTENTION: Votre créature est malade et perd de la santé! ⚠️")

    print("\n")