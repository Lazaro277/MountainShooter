![alt text](https://github.com/Lazaro277/MountainShooter/blob/8527a921d2c33755f4ff3ef5e1fb4ff70d0cfc89/asset/Player1.png) Mountain Shooter ![alt text](https://github.com/Lazaro277/MountainShooter/blob/8527a921d2c33755f4ff3ef5e1fb4ff70d0cfc89/asset/Player1.png)
===============

Mountain Shooter is a 2D arcade shooter game developed in **Python** using **Pygame**.

The game features two levels, different enemies, a scoring system, local multiplayer modes, sound effects, background music, and score storage using SQLite.

## 🎮 About the Game

In Mountain Shooter, the player controls a character while facing enemies throughout two different levels.

The game includes:

- Single-player mode
- Two-player cooperative mode
- Two-player competitive mode
- Two different levels
- Different enemy types
- Shooting and collision system
- Health system
- Score system
- Local ranking stored with SQLite
- Background music and sound effects

## 📸 Screenshots

### Main Menu

![Mountain Shooter Main Menu](https://github.com/user-attachments/assets/c9524f59-6ebd-443a-82c0-53b63eb2128f)

### Level 1

![Mountain Shooter Level 1](https://github.com/user-attachments/assets/8af63514-178d-44c9-9eb0-299e0aee0933)

## 🛠️ Technologies

The project was developed using:

- Python
- Pygame Community Edition
- SQLite
- Object-Oriented Programming (OOP)
- Git
- GitHub

## 📂 Project Structure

```text
MountainShooter/
│
├── asset/
│   ├── images
│   ├── music
│   └── game assets
│
├── code/
|   ├── AssetPath.py
│   ├── Background.py
│   ├── Const.py
│   ├── DBProxy.py
│   ├── Enemy.py
│   ├── EnemyShot.py
│   ├── Entity.py
│   ├── EntityFactory.py
│   ├── EntityMediator.py
│   ├── Game.py
│   ├── Level.py
│   ├── Menu.py
│   ├── Player.py
│   ├── PlayerShot.py
│   ├── Score.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 How to Run

### Requirements

Before running the game, make sure you have **Python** installed on your computer.

You can check your Python installation with:

```bash
python --version
```

### 1. Clone the repository

```bash
git clone https://github.com/Lazaro277/MountainShooter.git
```

### 2. Open the project folder

```bash
cd MountainShooter
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the game

```bash
python main.py
```

The game window should open after running the command.

## 🕹️ Controls

### Player 1

| Action | Key |
|---|---|
| Move Up | ↑ |
| Move Down | ↓ |
| Move Left | ← |
| Move Right | → |
| Shoot | Right Ctrl |

### Player 2

| Action | Key |
|---|---|
| Move Up | W |
| Move Down | S |
| Move Left | A |
| Move Right | D |
| Shoot | Left Ctrl |

## 🏆 Score System

The game includes a local score system.

Player scores are stored using **SQLite**, allowing the game to maintain a ranking of the highest scores.

The **SCORE** option in the main menu displays the saved ranking.

## 🧠 Concepts Practiced

This project was developed as a practical way to apply programming concepts such as:

- Object-Oriented Programming
- Classes and inheritance
- Abstract classes
- Game loops
- Event handling
- Collision detection
- Entity management
- Database integration
- Modular code organization
- Version control with Git and GitHub

## 📚 What I Learned

During the development of Mountain Shooter, I practiced structuring a Python project using multiple classes and modules instead of keeping the entire game in a single file.

The project also helped me better understand how different parts of an application communicate with each other, including players, enemies, projectiles, levels, menus, collision systems, and database operations.

## 🤝 Contributions

Suggestions and contributions are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

## 👨‍💻 Author

Developed by **Lázaro Messias** as part of my studies and practice in software development.

If you liked the project, feel free to leave a ⭐ on the repository.
