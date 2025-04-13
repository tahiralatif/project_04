import random


"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

Num_sides = 6  # Number of sides on the die
def roll_dice():
    """Simulates rolling two diece and prin theri total."""

    num1: int = random.randint(1, Num_sides)
    num2 : int = random.randint(1, Num_sides)
    total = num1 + num2
    print(f"die1 {num1} + die2 {num2} = Total of two dice {total}")

def main():
    die1 = 10
    
    print(f"Die1 in main is start as {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
if __name__ == "__main__":
    main()