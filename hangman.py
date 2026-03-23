import random

words = ["python", "code", "intern", "data", "model"]
word = random.choice(words)

guessed = []
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print(f"Wrong guess! Tries left: {tries}")

if tries == 0:
    print("💀 You lost! Word was:", word)