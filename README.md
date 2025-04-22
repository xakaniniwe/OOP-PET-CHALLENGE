# OOP Pet Challenge

This repository contains the solution to the OOP Pet Challenge. Unfortunately the Group I am Assignt to is inactive so i had to do it alone

## Overview

The challenge involved creating a Python class named `Pet` with specific attributes (name, hunger, energy, happiness) and methods (eat, sleep, play, get_status, train, show_tricks). The goal was to implement this class in `pet.py` and then demonstrate its functionality in `main.py` by creating a `Pet` object named "Nini.Explorer" and interacting with it in an engaging way, including teaching it explorer-themed tricks.

## File Structure

.
├── main.py     # Contains the script to create and interact with the Pet object "Nini.Explorer" with engaging output and trick learning.
└── pet.py      # Contains the definition of the Pet class.
└── README.md   # This file, providing information about the project.
└── output.png  # (Optional) Screenshot of the program output.


## `pet.py`

This file defines the `Pet` class with the following attributes and methods:

**Attributes:**

* `name`: The name of the pet (string).
* `hunger`: An integer representing the hunger level (0 = full, 10 = very hungry).
* `energy`: An integer representing the energy level (0 = tired, 10 = fully rested).
* `happiness`: An integer representing the happiness level (0-10).
* `tricks`: A list to store the tricks the pet has learned.

**Methods:**

* `__init__(self, name)`: Initializes a new `Pet` object with a given name and sets initial hunger, energy, and happiness levels.
* `eat(self)`: Reduces hunger by 3 (min 0) and increases happiness by 1 (max 10).
* `sleep(self)`: Increases energy by 5 (max 10).
* `play(self)`: Decreases energy by 2 (min 0), increases happiness by 2 (max 10), and increases hunger by 1 (max 10).
* `get_status(self)`: Prints the current status of the pet (hunger, energy, happiness, and learned tricks).
* `train(self, trick)`: Teaches the pet a new trick (if not already learned) and stores it in the `tricks` list.
* `show_tricks(self)`: Prints all the tricks the pet has learned.

## `main.py`

This file demonstrates the usage of the `Pet` class by creating a `Pet` object named "Nini.Explorer" and simulating interactions with it. The output is designed to be more engaging, showing Nini.Explorer eating, playing, sleeping, and learning explorer-themed tricks one by one with descriptive messages and pauses.

```python
from pet import Pet
import time  # To add pauses and make it more engaging

if __name__ == "__main__":
    nini = Pet("Nini.Explorer")
    nini.get_status()

    print("Let's start our adventure with Nini.Explorer!\n")
    time.sleep(1)

    print("Nini.Explorer is feeling a bit peckish...")
    nini.eat()
    nini.get_status()
    time.sleep(1.5)

    print("Time for some exploration!")
    nini.play()
    nini.get_status()
    time.sleep(1.5)

    print("Nini.Explorer needs some rest after all that excitement...")
    nini.sleep()
    nini.get_status()
    time.sleep(2)

    print("\n--- Training Session ---")

    print("\nLet's try teaching Nini.Explorer a new skill...")
    trick1 = "spot hidden trails"
    print(f"Teaching '{trick1}'...")
    nini.train(trick1)
    nini.get_status()
    time.sleep(2)

    print("\nAnother useful explorer skill to learn...")
    trick2 = "identify rare plants"
    print(f"Teaching '{trick2}'...")
    nini.train(trick2)
    nini.get_status()
    time.sleep(2)

    print("\nOne more for today's lesson...")
    trick3 = "signal for help"
    print(f"Teaching '{trick3}'...")
    nini.train(trick3)
    nini.get_status()
    time.sleep(2)

    print("\nNini.Explorer remembers all the new tricks!")
    nini.show_tricks()
    time.sleep(1)

    print("\nAfter a long day of learning, Nini.Explorer plays some more...")
    nini.play()
    nini.get_status()
    time.sleep(1.5)

    print("Time for a good meal to replenish energy!")
    nini.eat()
    nini.eat()
    nini.get_status()

    print("\nNini.Explorer is ready for more adventures tomorrow!")
