import random
import time


def trigger_random_event(creature):
    weather_events = [
        {"name": "beau temps", "effect": lambda c: {"happiness": 2},
         "message": "profite du beau temps et se sent heureux !"},
        {"name": "pluie", "effect": lambda c: {"energy": -1, "happiness": -1},
         "message": "est trempé par la pluie et se sent un peu malheureux..."},
        {"name": "orage", "effect": lambda c: {"happiness": -3}, "message": "a peur de l'orage et se cache !"},
        {"name": "neige", "effect": lambda c: {"energy": -2, "health": -1}, "message": "a froid à cause de la neige !"},
        {"name": "chaleur", "effect": lambda c: {"energy": -2, "hunger": -2},
         "message": "souffre de la chaleur et se fatigue plus vite..."}
    ]

    encounter_events = [
        {"name": "ami", "effect": lambda c: {"happiness": 5},
         "message": "a rencontré un nouvel ami et s'est beaucoup amusé !"},
        {"name": "ennemi", "effect": lambda c: {"happiness": -3, "energy": -2},
         "message": "a croisé un ennemi et a dû s'enfuir !"},
        {"name": "étranger", "effect": lambda c: {"happiness": -1},
         "message": "a rencontré un étranger et était un peu méfiant..."},
        {"name": "groupe", "effect": lambda c: {"happiness": 3, "energy": -3},
         "message": "a joué avec un groupe d'amis mais est maintenant fatigué !"}
    ]

    discovery_events = [
        {"name": "trésor", "effect": lambda c: {"happiness": 4},
         "message": "a trouvé un petit trésor et est tout excité !"},
        {"name": "nourriture", "effect": lambda c: {"hunger": 3}, "message": "a trouvé un petit encas !"},
        {"name": "jouet", "effect": lambda c: {"happiness": 3, "energy": -1},
         "message": "a trouvé un nouveau jouet et s'amuse bien !"},
        {"name": "cachette", "effect": lambda c: {"energy": 2},
         "message": "a découvert une cachette confortable pour se reposer."}
    ]

    event_type = random.choices(
        ["weather", "encounter", "discovery", "none"],
        weights=[30, 25, 25, 20],
        k=1
    )[0]

    if event_type == "none":
        return ""

    if event_type == "weather":
        event = random.choice(weather_events)
    elif event_type == "encounter":
        event = random.choice(encounter_events)
    else:
        event = random.choice(discovery_events)

    effects = event["effect"](creature)
    message = f"{creature.name} {event['message']}"

    for stat, value in effects.items():
        if stat == "health":
            if value > 0:
                old_health = creature.health
                creature.heal(value)
                message += f" (+{creature.health - old_health} santé)"
            else:
                old_health = creature.health
                creature.damage(abs(value))
                message += f" (-{old_health - creature.health} santé)"
        elif stat == "hunger":
            old_hunger = creature.hunger
            creature.hunger = max(0, min(creature.max_hunger, creature.hunger + value))
            if value > 0:
                message += f" (+{creature.hunger - old_hunger} satiété)"
            else:
                message += f" (-{old_hunger - creature.hunger} satiété)"
        elif stat == "energy":
            old_energy = creature.energy
            creature.energy = max(0, min(creature.max_energy, creature.energy + value))
            if value > 0:
                message += f" (+{creature.energy - old_energy} énergie)"
            else:
                message += f" (-{old_energy - creature.energy} énergie)"
        elif stat == "happiness":
            old_happiness = creature.happiness
            creature.happiness = max(0, min(creature.max_happiness, creature.happiness + value))
            if value > 0:
                message += f" (+{creature.happiness - old_happiness} bonheur)"
            else:
                message += f" (-{old_happiness - creature.happiness} bonheur)"

    if event_type == "weather" and random.random() < 0.2 and not creature.is_sick:
        creature.get_sick()
        message += f"\n{creature.name} est tombé malade à cause de cet événement !"

    return message


def display_random_event(creature):
    event_message = trigger_random_event(creature)

    if event_message:
        print("\n=== ÉVÉNEMENT ALÉATOIRE ===")
        print(event_message)
        time.sleep(2)