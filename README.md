# Tamagotchi 🐾

## About

Tamagotchi is a Python-based virtual pet simulation game where players care for a digital creature, managing its daily needs and interactions. Experience the challenges of keeping a virtual companion happy, healthy, and alive through various mini-games and dynamic events.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Author](#author)
- [License](#license)

## Installation

Follow these steps to set up the project on your local machine:

```bash
# Clone the repository
git clone https://github.com/Xplit495/tamagotchi-python-oop.git

# Navigate to the project directory
cd tamagotchi-python-oop

# Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

## Usage

Start the game by running the main script:

```bash
python main.py
```

Optional: Load a previous save game
```bash
python main.py -s saves/your_save_file.save
```

## Features

### Core Gameplay
- Create a virtual pet from multiple species (Dog, Cat, Dragon, Rabbit, Hamster, Fox, Penguin, Panda, Baby Turtle)
- Manage your pet's vital statistics:
  - Health
  - Hunger
  - Energy
  - Happiness

### Interactive Mini-Games
- **Feeding**: Choose from healthy and unhealthy food options
- **Playing**: Engage in a hide-and-seek style mini-game
- **Healing**: Play Tic-Tac-Toe to win medical spray
- **Curing**: Play Hangman to obtain a remedy

### Dynamic Events
- Random events affect your pet's stats
- Weather conditions
- Social encounters
- Unexpected discoveries

### Advanced Mechanics
- Creature lifecycle (Baby → Child → Adult)
- Random illness mechanics
- Saving and loading game progress

## Dependencies

- Python 3.10+
- inquirerpy
- keyboard

## Author

**Carrola Quentin**
- GitHub: [Xplit495](https://github.com/Xplit495)
- LinkedIn: [Quentin Carrola](https://www.linkedin.com/in/quentin-carrola-24306b304/)
- Email: carrolaquentin.pro@gmail.com

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Tamagotchi is a parody-style virtual pet game. Enjoy responsibly! 😄🎮