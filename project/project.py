# CS50P Final Project - Wordle
# Authors: Andres Elizondo and Sabrina Ramirez Libertella

import random
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama so colors work on all platforms
init(autoreset=True)

# Game settings
WORD_LENGTH = 5
MAX_GUESSES = 6


def load_word_list(filepath="words.txt"):
    # Read words from the file and return a list of valid 5-letter words
    if not open(filepath, "r"):
        print("Error: words.txt not found.")
        sys.exit(1)

    words = []
    with open(filepath, "r") as file:
        for line in file:
            word = line.strip().upper()
            if len(word) == WORD_LENGTH and word.isalpha():
                words.append(word)

    if len(words) == 0:
        print("Error: no valid words found in words.txt")
        sys.exit(1)

    return words


def get_random_word(word_list):
    # Pick and return a random word from the list
    if len(word_list) == 0:
        raise ValueError("word_list is empty")
    return random.choice(word_list)


def check_guess(guess, target):
    # Compare the guess to the target word
    # Returns a list of tuples: (letter, "correct"/"present"/"absent")
    guess = guess.upper()
    target = target.upper()

    result = [None] * WORD_LENGTH
    target_remaining = list(target)

    # First pass: find letters in the correct position
    for i in range(WORD_LENGTH):
        if guess[i] == target[i]:
            result[i] = (guess[i], "correct")
            target_remaining[i] = None

    # Second pass: find letters in the wrong position
    for i in range(WORD_LENGTH):
        if result[i] is not None:
            continue
        if guess[i] in target_remaining:
            result[i] = (guess[i], "present")
            target_remaining[target_remaining.index(guess[i])] = None
        else:
            result[i] = (guess[i], "absent")

    return result


def is_valid_word(word, word_list):
    # Check if the word is 5 letters and exists in our word list
    word = word.strip().upper()
    if len(word) != WORD_LENGTH:
        return False
    if not word.isalpha():
        return False
    if word not in word_list:
        return False
    return True


def format_feedback(result):
    # Turn the result into a colored string for the terminal
    output = ""
    for letter, status in result:
        if status == "correct":
            output += Back.GREEN + Fore.BLACK + " " + letter + " " + Style.RESET_ALL + " "
        elif status == "present":
            output += Back.YELLOW + Fore.BLACK + " " + letter + " " + Style.RESET_ALL + " "
        else:
            output += Back.WHITE + Fore.BLACK + " " + letter + " " + Style.RESET_ALL + " "
    return output


def display_header():
    # Print the welcome banner
    print()
    print(Fore.CYAN + Style.BRIGHT + "╔══════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "║      🟩 W O R D L E      ║")
    print(Fore.CYAN + Style.BRIGHT + "╚══════════════════════════╝")
    print()
    print("Guess the 5-letter word in 6 tries.")
    print(Back.GREEN  + Fore.BLACK + " G " + Style.RESET_ALL + " = correct position")
    print(Back.YELLOW + Fore.BLACK + " Y " + Style.RESET_ALL + " = wrong position")
    print(Back.WHITE  + Fore.BLACK + " W " + Style.RESET_ALL + " = not in word")
    print()


def display_board(history):
    # Print all previous guesses with their colors
    for i in range(len(history)):
        print("  Guess " + str(i + 1) + ": " + format_feedback(history[i]))
    # Print empty rows for remaining guesses
    for i in range(MAX_GUESSES - len(history)):
        print("  · · · · ·")
    print()


def main():
    # Load the word list
    word_list = load_word_list()

    display_header()

    # Main game loop — keeps playing until the user says no
    while True:
        target = get_random_word(word_list)
        history = []
        won = False

        print("A new word has been chosen. Good luck!\n")

        for attempt in range(1, MAX_GUESSES + 1):
            display_board(history)

            # Ask the player for a valid guess
            guess = ""
            while True:
                guess = input("  Attempt " + str(attempt) + "/" + str(MAX_GUESSES) + " ➜  ").strip()
                if is_valid_word(guess, word_list):
                    break
                elif len(guess) != WORD_LENGTH:
                    print(Fore.RED + "  Please enter a 5-letter word.")
                else:
                    print(Fore.RED + "  That word is not in the list. Try another.")

            # Check the guess and save it
            result = check_guess(guess, target)
            history.append(result)

            # Check if the player won
            correct_count = 0
            for letter, status in result:
                if status == "correct":
                    correct_count += 1

            if correct_count == WORD_LENGTH:
                display_board(history)
                print(Fore.GREEN + Style.BRIGHT + "  🎉 Correct! You got it in " + str(attempt) + " guesses!")
                won = True
                break

        # If player didn't win, reveal the word
        if not won:
            display_board(history)
            print(Fore.RED + Style.BRIGHT + "  😞 Better luck next time! The word was: " + target)

        # Ask to play again
        print()
        again = input("  Play again? (y/n) ➜  ").strip().lower()
        if again != "y" and again != "yes":
            print(Fore.CYAN + "\n  Thanks for playing Wordle! Goodbye. 👋\n")
            break
        print()


if __name__ == "__main__":
    main()