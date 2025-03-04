import random
from abc import ABC, abstractmethod
from models.food import Food


class Creature(ABC):
    """
    Classe abstraite qui définit le comportement de base de toutes les créatures virtuelles.

    Cette classe gère les attributs vitaux (santé, faim, énergie, bonheur),
    les transitions d'état de vie, et les interactions de base comme manger, jouer et dormir.

    Attributes:
        name (str): Nom de la créature
        max_health (int): Santé maximale
        health (int): Santé actuelle
        max_hunger (int): Satiété maximale
        hunger (int): Satiété actuelle
        max_energy (int): Énergie maximale
        energy (int): Énergie actuelle
        max_happiness (int): Bonheur maximal
        happiness (int): Bonheur actuel
        is_sick (bool): Indique si la créature est malade
        is_alive (bool): Indique si la créature est en vie
        alive_days (int): Nombre de jours de vie
        stage (str): Stade de développement ("bébé", "enfant", "adulte", "mort")
    """

    def __init__(self, name, max_health, max_hunger, max_energy, max_happiness):
        """
        Initialise une nouvelle créature avec ses attributs vitaux.

        Args:
            name (str): Nom de la créature
            max_health (int): Santé maximale
            max_hunger (int): Satiété maximale
            max_energy (int): Énergie maximale
            max_happiness (int): Bonheur maximal
        """
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.hunger = max_hunger
        self.max_hunger = max_hunger
        self.max_energy = max_energy
        self.energy = max_energy
        self.max_happiness = max_happiness
        self.happiness = max_happiness
        self.is_sick = False
        self.is_alive = True
        self.alive_days = 1
        self.stage = "bébé"

    def heal(self, heal_gain):
        """
        Augmente la santé de la créature, sans dépasser le maximum.

        Args:
            heal_gain (int): Points de santé à ajouter
        """
        self.health += heal_gain
        if self.health > self.max_health:
            self.health = self.max_health

    def damage(self, damage):
        """
        Diminue la santé de la créature et vérifie si elle meurt.

        Args:
            damage (int): Points de santé à retirer
        """
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def feed(self, food: Food):
        """
        Nourrit la créature avec un aliment, affectant sa satiété et sa santé.

        Args:
            food (Food): L'objet nourriture à donner à la créature
        """
        # Augmenter la satiété
        self.hunger += food.satiety
        if self.hunger > self.max_hunger:
            self.hunger = self.max_hunger

        # Effet sur la santé selon la qualité de la nourriture
        if food.is_good_quality:
            self.heal(food.health_effect)
        else:
            self.damage(food.health_effect)

    def starve(self, hunger):
        """
        Fait perdre de la satiété à la créature et vérifie si elle meurt de faim.

        Args:
            hunger (int): Points de satiété à retirer
        """
        self.hunger -= hunger
        if self.hunger < 0:
            self.hunger = 0
            self.health = 0  # La créature meurt de faim
            self.is_alive = False

    def sleep(self, energy, lose_hunger):
        """
        Fait dormir la créature, augmentant son énergie mais diminuant sa satiété.

        Args:
            energy (int): Points d'énergie à récupérer
            lose_hunger (int): Points de satiété perdus pendant le sommeil
        """
        self.energy += energy
        self.hunger -= lose_hunger
        if self.energy > self.max_energy:
            self.energy = self.max_energy
        self.starve(lose_hunger)  # Vérifier si la perte de satiété est critique

    def play(self, happiness, lose_energy):
        """
        Fait jouer la créature, augmentant son bonheur mais diminuant son énergie.

        Args:
            happiness (int): Points de bonheur à gagner
            lose_energy (int): Points d'énergie dépensés
        """
        self.happiness += happiness
        self.energy -= lose_energy
        if self.happiness > self.max_happiness:
            self.happiness = self.max_happiness
        if self.energy < 0:
            self.energy = 0

    def get_sick(self):
        """
        Rend la créature malade.
        """
        self.is_sick = True

    def cure(self):
        """
        Guérit la créature de sa maladie.
        """
        self.is_sick = False

    def grow(self):
        """
        Fait évoluer la créature selon son âge.

        Les transitions se font à 20 jours (enfant), 50 jours (adulte)
        et 100 jours (mort de vieillesse).
        """
        if self.alive_days == 20:
            self.stage = "enfant"
        elif self.alive_days == 50:
            self.stage = "adulte"
        elif self.alive_days == 100:
            self.stage = "mort"
            self.is_alive = False

    def time_pass(self):
        """
        Simule le passage du temps pour la créature.

        Réduit la satiété, l'énergie et le bonheur de manière aléatoire,
        fait vieillir la créature, et gère les probabilités de tomber malade.
        """
        # Diminution aléatoire de la satiété (1-3 points)
        hunger_loss = random.randint(1, 3)
        self.starve(hunger_loss)

        # Diminution aléatoire de l'énergie (1-2 points)
        energy_loss = random.randint(1, 2)
        self.energy = max(0, self.energy - energy_loss)

        # Diminution aléatoire du bonheur (1-2 points)
        happiness_loss = random.randint(1, 2)
        self.happiness = max(0, self.happiness - happiness_loss)

        # Vieillissement et évolution
        self.alive_days += 1
        self.grow()

        # Calcul de la probabilité de tomber malade
        sick_probability = random.randint(1, 100)
        base_chance = 5  # 5% de chance par défaut

        # La probabilité augmente si la créature a faim
        if self.hunger < self.max_hunger * 0.3:
            base_chance += 3

        # La probabilité augmente si la créature est malheureuse
        if self.happiness < self.max_happiness * 0.3:
            base_chance += 2

        # Vérifier si la créature tombe malade
        if 1 <= sick_probability <= base_chance and not self.is_sick:
            self.get_sick()

        # Effets de la maladie
        if self.is_sick:
            self.damage(1)  # Perte de santé
            self.energy = max(0, self.energy - 1)  # Perte d'énergie
            self.happiness = max(0, self.happiness - 1)  # Perte de bonheur

    def check_critical_status(self):
        """
        Vérifie si les attributs vitaux de la créature sont dans un état critique.

        Returns:
            list: Liste des messages d'alerte pour chaque attribut critique
        """
        alerts = []

        # Définir les seuils critiques et de préavis
        CRITICAL_THRESHOLD = 0.2  # 20% du maximum
        LOW_THRESHOLD = 0.3  # 30% du maximum

        # Vérifier la santé
        health_percentage = self.health / self.max_health
        if health_percentage <= CRITICAL_THRESHOLD:
            alerts.append(f"⚠️ CRITIQUE : {self.name} est gravement malade et a besoin de soins urgents !")
        elif health_percentage <= LOW_THRESHOLD:
            alerts.append(f"⚠️ ATTENTION : La santé de {self.name} est faible !")

        # Vérifier la satiété
        hunger_percentage = self.hunger / self.max_hunger
        if hunger_percentage <= CRITICAL_THRESHOLD:
            alerts.append(f"⚠️ CRITIQUE : {self.name} est affamé et risque de mourir de faim !")
        elif hunger_percentage <= LOW_THRESHOLD:
            alerts.append(f"⚠️ ATTENTION : {self.name} a très faim !")

        # Vérifier l'énergie
        energy_percentage = self.energy / self.max_energy
        if energy_percentage <= CRITICAL_THRESHOLD:
            alerts.append(f"⚠️ CRITIQUE : {self.name} est complètement épuisé et doit dormir !")
        elif energy_percentage <= LOW_THRESHOLD:
            alerts.append(f"⚠️ ATTENTION : {self.name} est très fatigué !")

        # Vérifier le bonheur
        happiness_percentage = self.happiness / self.max_happiness
        if happiness_percentage <= CRITICAL_THRESHOLD:
            alerts.append(f"⚠️ CRITIQUE : {self.name} est déprimé et a besoin de jouer immédiatement !")
        elif happiness_percentage <= LOW_THRESHOLD:
            alerts.append(f"⚠️ ATTENTION : {self.name} est malheureux !")

        return alerts

    @abstractmethod
    def make_sound(self):
        """
        Méthode abstraite que chaque sous-classe doit implémenter.
        Retourne le son caractéristique de la créature.

        Returns:
            str: Le son émis par la créature
        """
        pass