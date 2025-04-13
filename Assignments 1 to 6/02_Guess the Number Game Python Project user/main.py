import random

def main():
    while True:
        user_input = input("\nEnter a number between 1 and 20 or type 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break

        try:
            user_guess = int(user_input)
            if user_guess < 1 or user_guess > 20:
                print("Please enter a number between 1 and 20.")
                continue

            computer_guess = random.randint(1, 20)

            if user_guess == computer_guess:
                print(f"🎉 Congratulations! You guessed the correct number: {computer_guess}")
            elif user_guess < computer_guess:
                print(f"user guess Too low! The correct number was computer guess {computer_guess}.")
            else:
                print(f"Too high! The correct number was computer guess {computer_guess}.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20, or type 'exit' to quit.")

main()
