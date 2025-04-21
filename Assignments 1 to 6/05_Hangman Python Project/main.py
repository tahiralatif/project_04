import random

# 🔤 Word list (you can add more!)
word_list = ['python', 'hangman', 'challenge', 'developer', 'keyboard']

# 🎯 Choose random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# 🧍 Lives (wrong attempts allowed)
lives = 6

# ⬜ Create display for blanks like _ _ _ _
display = ['_'] * word_length

# ✅ To track already guessed letters
guessed_letters = []

print("🎮 Welcome to Hangman!")
print(" ".join(display))

# 🔁 Main game loop
# 🔁 Main game loop
while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter *only one* letter (a-z).")
        continue

    if guess in guessed_letters:
        print(f"❗ You've already guessed '{guess}'")
        continue
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct!")
    else:
        lives -= 1
        print(f"❌ Wrong! You lost a life. Lives left: {lives}")

    print(" ".join(display))
    print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f" ❗ You've already guessed '{guess}'")
        continue
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct!")
    else:
        lives -= 1
        print(f"❌ Wrong! You lost a life. Lives left: {lives}")

    print(" ".join(display))
    print(f"Guessed letters: {', '.join(guessed_letters)}\n")

# 🎉 Result
if '_' not in display:
    print("🏆 Congratulations! You won 🎉")
else:
    print(f"💀 Game over! The word was: {chosen_word}")
print("Thanks for playing! 👋")