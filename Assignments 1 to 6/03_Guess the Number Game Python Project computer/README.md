# 🎯 Computer Guess Game (Python)

A command-line Python game where the computer tries to guess a number you're thinking of using **binary search logic**.

---

## 📌 Overview

This interactive game challenges the computer to guess a number between **1 and 20** that the user has in mind.  
The user provides feedback on each guess:

- `too low`
- `too high`
- `correct`

Based on your feedback, the computer adjusts its range and keeps guessing until it finds the correct number.

---

## ⚙️ How It Works

1. The computer starts with a range of numbers from **1 to 20**.
2. It guesses the middle number of the current range.
3. You respond with:
   - **"too low"** → The actual number is higher.
   - **"too high"** → The actual number is lower.
   - **"correct"** → The computer guessed your number!
4. The computer updates its range based on your feedback and repeats the process.

---

## 🧪 Example

Think of a number between 1 and 20, and I will try to guess it! Just reply with 'too low', 'too high', or 'correct'.

My guess is: 10 Is it too low, too high, or correct? too high

My guess is: 5 Is it too low, too high, or correct? too low

My guess is: 7 Is it too low, too high, or correct? correct

🎉 Yay! I guessed your number in 3 tries!

python
Copy
Edit

---

## ✨ Features

- 🖥️ Simple command-line interface
- 🧠 Smart guessing using binary search algorithm
- 🚫 Handles invalid inputs
- 🐍 Easy to run in any Python 3 environment

---

## 💻 Code

```python
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
🧾 Requirements
Python 3.x

👩‍💻 Author
Tahira
Aspiring Software Developer | Passionate about building smart and interactive Python projects 💡