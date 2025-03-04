import random

from utils.clear_terminal import clear_terminal
from utils.print_ascii_art import print_ascii_art


def display_creature_status(creature):
    """
    Affiche l'état détaillé de la créature avec une interface utilisateur riche.

    Cette fonction génère un rapport complet sur l'état de la créature, comprenant :
    - Un art ASCII représentant la créature
    - Des informations générales (nom, âge, stade)
    - Une représentation graphique des statistiques principales
    - Des alertes et messages d'état

    Args:
        creature (Creature): L'objet créature dont on souhaite afficher le statut.

    Fonctionnalités principales :
    - Représentation visuelle des statistiques via des barres de progression
    - Indicateurs d'état critique pour chaque statistique
    - Messages dynamiques basés sur l'état général de la créature
    - Alertes spécifiques en cas de problème de santé
    """
    # Nettoie le terminal avant l'affichage
    clear_terminal()

    # Affiche l'art ASCII de la créature
    print_ascii_art(creature)

    # Affiche les informations de base
    print(f"========= {creature.name} =========")
    print(f"En vie depuis : {creature.alive_days} jours | Stade: {creature.stage}")
    print("-" * 40)

    # Définition des statistiques à afficher
    stats = [
        {"name": "Santé", "value": creature.health, "max": creature.max_health},
        {"name": "Faim", "value": creature.hunger, "max": creature.max_hunger},
        {"name": "Énergie", "value": creature.energy, "max": creature.max_energy},
        {"name": "Bonheur", "value": creature.happiness, "max": creature.max_happiness}
    ]

    # Affichage des statistiques avec barres de progression
    for stat in stats:
        # Calcul de la barre de progression
        percentage = int((stat["value"] / stat["max"]) * 10)
        bar = "█" * percentage + "░" * (10 - percentage)

        # Ajout d'indicateurs d'état critique
        status_indicator = ""
        if percentage <= 2:
            status_indicator = "⚠️"
        elif percentage <= 3:
            status_indicator = "⚠"

        # Affichage de la statistique
        print(f"{stat['name']:8} [{bar}] {stat['value']}/{stat['max']} {status_indicator}")

    # Vérification des alertes critiques
    alerts = creature.check_critical_status()

    # Affichage des alertes s'il y en a
    if alerts:
        print("\n=== ALERTES ===")
        for alert in alerts:
            print(alert)

    # Alerte spéciale en cas de maladie
    if creature.is_sick:
        print("\n⚠️  ATTENTION: Votre créature est malade et perd de la santé! ⚠️")

    # Calcul du pourcentage moyen des statistiques
    avg_percentage = (creature.health / creature.max_health +
                      creature.hunger / creature.max_hunger +
                      creature.energy / creature.max_energy +
                      creature.happiness / creature.max_happiness) / 4

    # Messages dynamiques basés sur l'état général
    print("\n" + "-" * 40)
    if avg_percentage > 0.8:
        # État excellent
        messages = [
            f"{creature.name} est en pleine forme !",
            f"{creature.name} semble très heureux aujourd'hui !",
            f"{creature.name} déborde d'énergie et de vitalité !"
        ]
        print(random.choice(messages))
    elif avg_percentage > 0.5:
        # État bon
        messages = [
            f"{creature.name} se porte plutôt bien.",
            f"{creature.name} semble content.",
            f"{creature.name} est dans un état correct."
        ]
        print(random.choice(messages))
    elif avg_percentage > 0.3:
        # État préoccupant
        messages = [
            f"{creature.name} ne se sent pas très bien...",
            f"{creature.name} a besoin de votre attention.",
            f"{creature.name} pourrait aller mieux."
        ]
        print(random.choice(messages))
    else:
        # État critique
        messages = [
            f"{creature.name} est dans un état inquiétant !",
            f"{creature.name} a besoin de soins urgents !",
            f"{creature.name} ne tiendra plus longtemps dans cet état !"
        ]
        print(random.choice(messages))

    print("\n")