Group Project - War Game
==========================
[![Documentation Status](https://readthedocs.org/projects/a-python-project-template-codestyle-and-linters-included/badge/?version=latest)](https://a-python-project-template-codestyle-and-linters-included.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Group project, written by A Almerhaj, J Nilsson and B Sadiku.

[[_TOC_]]

# Introduction
--------------------------
This Group project was written in HT25 to be submitted for Examination 2 of the course **Methods of Sustainable Programming** - **DA214A**.

The main goal with this project was to write a small Terminal game in line with the requirements presented in the Examination. With a focus on teamwork, OOP and unittesting.

**OBS!** Note that instructions for the following segments were written with Git Bash in mind, meaning that the commands may not look the exact same for a different Terminal.

Furthermore, the documentation for this project makes heavy use of __Make__, which can be installed using [Chocolatey](https://chocolatey.org/install)

To install Make using the terminal
```
Choco install make
```


# Installation
--------------------------
There are two main ways to install the game:
- Download the game as a Zip file and Unzip
- Clone the Repo

Once installed, open your terminal and navigate to the main directory:
```
cd /*filepath here*/Sustainable_development_assignment_2/
```
*replace 'filepath here' with your filepath to the game, including the asterisks*

### Downloading a Zip file
--------------------------
To download the zip file, either navigate to the latest release and download it from there. Or click the big green 'Code' button, which will open a drop down menu with a download option.

Once downloaded simply unzip the file with your tool of choice.


### Cloning a Repo
--------------------------
To clone the repo, simply open the terminal and enter

```
git clone https://github.com/CopycatPandaExpressChowMein/Sustainable_development_assignment_2.git
```

This will clone the report to the directory the terminal is currently open in.
### Installing Venv
--------------------------
In order to ensure that you have all the dependencies necessary, we recommend that you make sure you have a Python Virtual Environment (Venv for short) operational. A makefile with a make command is included with the project to make this as easy as possible. Simply do the following:

How to Install with the terminal
```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command deactivate.

### Installing dependencies
--------------------------
To install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the requirements.txt.
Do not forget to check that you have an active venv.

Using the terminal
```
# Do install them
make install

# Check what is installed
make installed
```

Additionally, in order to generate UMLs of the project, make sure that Graphviz is installed.

How to install Graphviz using the terminal
```
choco install Graphviz
```

# Running the game
--------------------------
In order to run the game, open your terminal and navigate to the main directory:

```
cd /*filepath here*/Sustainable_development_assignment_2/
```

Once the terminal is open in the right directory you can run it with the following:
```
python war/Main.py
```

# Basic Game Info
--------------------------
The key commands used in the game are:

- start
    - This command starts a new game, it will prompt you to select a game mode then name all the players
- draw/draw_card
    - This command progresses the game, and can only be executed once a game has started
- rules
    - This command prints the rules of the game.
- highscores
    - This command prints all highscores in memory.
- exit/quit/q
    - This command closes the game.
- namechange
    - This command lets a player change their name

### start
Running the start command tells the program to execute the start function in the Game class. Taking player input such as mode, names and ai difficulty as parameters. And then assigns the values in the game such as a deck of cards.

### draw/draw_card
Running the draw command tells the program to execute the draw_card function in the Game class. This function first compares the number of cards each player has to check if either still has cards left to play. After which it will print a series of GUI String elements, draw cards and compare them. In case a war occurs the function is recursively called to continue.

### Highscores
Highscores are loaded from a file in memory, if one doesn't exist it will be created the next time the game is saved. All highscores are saved as a dictionary in a json file, containing a player name and a list of wins that player has. After each finished game, new statistics are added to the player that won. Which can then be viewed by printing the highscores.

### Game mode
Upon starting a game the player(s) are prompted to select a game mode, either single player (1) or two-player (2). Depending on the choice you then name either 1 or both players, and if you selected single player you get to pick the difficulty of the AI.

### AI
The AI class functions almost exactly the same as a player. But has 3 difficulties
- Random 
    - Takes a random card from the deck.
- Top
    - Takes the top card in the deck (Default).
- Greedy
    - Always plays the highest card.

### Cheating
The player can cheat for testing purposes. This executes the cheat function in the Game class, which sets the value of all of their cards to 99. 

# Unit Testing
--------------------------
All main classes in the project have dedicated unittest files located in the test/ folder.
Tests verify that each class and method behaves correctly.

Run all tests using the terminal
```
make unittest
```

Run tests with coverage using the terminal
```
make coverage
```

Run linters and unittests with coverage using the terminal
```
make test
```

You can also run the tests for invidual classes using using the terminal
```
python -m unittest test.test_game
```



# Documentation
--------------------------
Documentation can be found in the ```doc/``` folder.

Generate documentation using the terminal
```
make pdoc
```

Generate documentation and UML using the terminal
```
make doc
```

# UML Diagrams
--------------------------
PNG of the UML diagrams can be found in the ```doc/``` folder.
**OBS!** Without __Graphviz__ installed the UML generation will fail.

![UML classes](/doc/uml/classes.png)

![UML packages](/doc/uml/packages.png)

Generate UML using the terminal
```
make pyreverse
```

Generate documentation and UML using the terminal
```
make doc
```