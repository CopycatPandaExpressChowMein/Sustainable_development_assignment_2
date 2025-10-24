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

# Installation
--------------------------
There are two main ways to install the game:
- Download the game as a Zip file and Unzip
- Clone the Repo

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

How to Install
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
```
# Do install them
make install

# Check what is installed
make installed
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
War is a simple two-player card game written in Python for Sustainable Development Assignment 2.
Each player draws cards; the higher value wins the round. If the cards are equal, a “war” occurs until one player wins all cards.


# Unit Testing
--------------------------

# Documentation
--------------------------

# UML Diagrams
--------------------------
