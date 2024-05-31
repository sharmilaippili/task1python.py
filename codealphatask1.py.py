import random

def choose_word():
  words = ["hangman", "computer", "programming", "python", "developer", "game", "player", "keyboard", "mouse", "monitor"]
  return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 10

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess! You have {} attempts left.".format(max_attempts - incorrect_guesses))
        else:
            print("Correct guess!")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word '{}' correctly!".format(word))
            break

    if incorrect_guesses == max_attempts:
        print("Sorry, you ran out of attempts. The word was '{}'.".format(word))

if __name__ == "_main_":
    hangman()