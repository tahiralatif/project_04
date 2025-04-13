import random


dice_art = {
    1: (
        "+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"
    ),
    2: (
        "+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"
    ),
    3: (
        "+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"
    ),
    4: (
        "+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"
    ),
    5: (
        "+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"
    ),
    6: (
        "+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+"
    )
}


def rolling_dice():
    dice_sides = 6

    while True:
        user_input = input("Enter Your Choice (r to roll, q to quit): ").strip().lower()

        if user_input == "r":
            dice1 = random.randint(1, dice_sides)
            dice2 = random.randint(1, dice_sides)
            total = dice1 + dice2
            print(f"Dice 1: {dice1}, Dice 2: {dice2}, Total: {total}\n")

            for line1 , line2 in zip(dice_art[dice1], dice_art[dice2]):
                print(f"{line1}  {line2}")      
        elif user_input == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'r' to roll or 'q' to quit.\n")

def main():
    print("🎲 Welcome to the Dice Rolling Game! 🎲")
    rolling_dice()

if __name__ == "__main__":
    main()
