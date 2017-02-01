# DiceSimulator

Dice simulator is a simple Dice Rolling Python3 App that runs on your command line.

## How to Use

The app will prompt you for the amount of *sides* that you want your dice to have, 
and will also ask how many *of this kind of dice* the user wants rolled.

The app will print the number of rolls, each roll's corresponding results, and the total sum of all results.

## Rerolling
Users will be prompted to either reroll dice or start a new dice roll. 

The user rerolls dice by entering a list of roll numbers separated by commas. 

For instance, if I had the following dice rolls:
```
Roll 1: 4
Roll 2: 7
Roll 3: 2
```
I would enter "1,3" to get new results for "Roll 1" and Roll 3."

## New Dice

To start a new dice roll, enter 0 when prompted to reroll dice.

## Quit

Exit the program by either terminal commands (ctrl-z or ctrl-c on linux) or inputing -1 instead of a positive integer.
