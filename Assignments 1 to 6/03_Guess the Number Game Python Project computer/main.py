def computer_guess_game():
    print("Think of a number between 1 and 20, and I will try to guess it!")
    print("Just reply with 'too low', 'too high', or 'correct'.\n")

    low = 1
    high = 20
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it too low, too high, or correct? ").lower()

        if feedback == "correct":
            print(f"🎉 Yay! I guessed your number in {attempts} tries!")
            break
        elif feedback == "too low":
            low = guess + 1
        elif feedback == "too high":
            high = guess - 1
        else:
            print("Please type only: 'too low', 'too high', or 'correct'.")

    else:
        print("Hmm, are you sure you gave honest feedback? 😅")

computer_guess_game()
