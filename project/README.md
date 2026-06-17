# Terminal Wordle
#### Video Demo: https://youtu.be/WOl3j9sJGRs?si=fivty5LeA7MoW7nm
#### Description:
## What is this project?
Terminal Wordle is an exact replica of Wordle entirely playable in your terminal.  The player has 6 chances to guess a random secret 5-letter word.  When guessing text after each guess the letter is either green for being in the correct position, yellow for incorrect position, or gray if not among any of the letters to be guessed.  The game continues until you win or run out of guesses at which point the game asks if you want to play again.

We chose to do this project because we both enjoy playing Wordle and thought it would challenge us properly to make the game playable using Python. This also presented an opportunity for us to practice many of the other concepts learned through-out this course, for example: functions, loops, file handling, string manipulation, testing using pytest, etc., etc.

---
## How to install and run
Step 1 Install dependencies:
```bash
pip install -r requirements.txt
```
This installs `colorama`, which adds color support to the terminal on all platforms (Windows, Mac, and Linux). Without it the game will not run. It also installs `pytest` which is needed to run the tests.

Step 2 Run the game:
```bash
python project.py
```
Step 3 Run the tests:
```bash
pytest test_project.py -v
```
---
## How to play
When you start the Game, you will be presented with a colorful banner that shows the color legend for the various tiles.  Next, a random 5-letter word has been randomly selected from our Word List. After guessing the Word, you press ENTER and your guess will appear in the Game Board with the appropriate tile colors:
- If you guess the letter exactly, (it is in the correct position), that tile will be color-coded GREEN.
- If you guess the letter correctly but NOT in the correct position, that tile will be color-coded YELLOW.
- If the letter is not in the word at all, that tile will be color-coded GREY.

You will be allowed to make 6 guesses to complete the Game and then you will receive a Congratulatory message from the Game with the number of attempts it took to guess the Correct Word. If you do not guess correctly after 6 attempts, the Correct word will be revealed to you.

Upon completion of the Game, the Game will provide you with one opportunity to play again.

---
## Files in this project
### `project.py`
This is the main file of the project, and it contains all the logic for the game. It includes the `main()` function and five other functions that each have a specific job.
### `load_word_list(filepath)`
This function opens the `words.txt` file and reads it one line at a time. It creates a list with all the valid 5-letter words and changes them to uppercase so that the program can compare words consistently.
If the file cannot be found, or if there are no valid words inside it, the program shows an error message and stops.
We decided to use a separate file for the words instead of writing them directly in the code. This makes the game easier to update because we can add or remove words without changing the actual Python script.

### `get_random_word(word_list)`
This function takes the list of words and randomly chooses one using Python’s built-in `random.choice()` function.
Before choosing a word, it checks that the list is not empty. If it is empty, the function raises a `ValueError`.
We kept this as a separate function because it makes the code easier to understand and also allows us to test the random word selection by itself.

### `check_guess(guess, target)`
This is the most important function in the game. It compares the player’s guess with the secret word and returns a list of tuples.
Each tuple contains a letter and one of three possible results: `"correct"`, `"present"`, or `"absent"`.
The function uses a two-pass approach to correctly handle duplicate letters. In the first pass, it checks which letters are in the correct position. In the second pass, it checks whether the remaining letters appear somewhere else in the word.
This is important because it prevents duplicate letters from being counted more than once and makes the game follow the official Wordle rules.

### `is_valid_word(word, word_list)`
This function checks if the player’s guess is valid.
It makes sure that the word has exactly 5 characters, contains only letters, and is included in the word list. It also removes any extra spaces before checking the word.
If the word does not meet these conditions, the function returns `False`, and the player has to enter a different word.

### `format_feedback(result)`
This function takes the result from `check_guess` and turns it into a colored string that can be shown in the terminal.
It uses the `colorama` library to give each letter a green, yellow, or white background depending on whether the letter is correct, present, or absent.
We separated this function from `check_guess` because they have different purposes. `check_guess` handles the game logic, while `format_feedback` handles how the result looks on the screen. This helps keep the code cleaner and easier to follow.

### `test_project.py`
This file contains 23 tests written with `pytest`. The tests are organized by function and cover a wide range of cases:
- All letters correct
- All letters absent
- Mixed correct, present, and absent letters
- Duplicate letters handled correctly
- Uppercase and lowercase input treated the same
- Words that are too short or too long rejected
- Words with numbers or symbols rejected
- Empty input rejected
- Whitespace stripped before validation
- Empty word list raises an error
- Missing file raises an error
- Random word always comes from the list
- Colored output contains the correct letters
We wrote these tests to make sure every function behaves correctly in both normal and edge case situations.
### `words.txt`
A plain text file with around 400 common 5-letter English words, one per line. This file is loaded at the start of every game. We chose common, everyday words so the game feels fair and familiar to any player.
### `requirements.txt`
Lists the two packages needed to run this project:
- `colorama` — required to display colors in the terminal
- `pytest` — required to run the test suite

---
## Design decisions
Why Colorama
Our goal was to provide the same color feedback as in the original game, Wordle. Colorama is the easiest way to have this functionality with no extra setup on your computer, regardless of whether you're running Windows, Mac. If we didn't use Colorama on your computer, then the color codes would show up as garbled letters/characters.

Why Two-pass algorithm  
Originally we began developing the function `check_guess` using a single-pass approach. It wasn't until we started testing it with guesses that contained repeated letters that we discovered issues when returning the correct answer. For example, if `STONE` is the answer and `SCENE` is the guess, then there is only ONE 'E' in the answer. Using a single-pass approach would have returned both 'E's from the guess. The solution was to use a two-pass approach: first, find and lock correct guess letter placements before checking letter placement with the remaining letters.

Why keep functions small and separate
We wanted each function of our application to have very clear purpose. Thus, `check_guess` only checks guessed letter placement, `format_feedback` only processes color feedback, and `is_valid_word` only validates guesses input by the user. This allowed us to perform each of our functional tests independently of the others (we tested each function by itself), so that when we found issues with functionality we could accurately identify where the issue was located in our code and address it.

Why load words from a file
Hard-coding hundreds of words directly in the Python script would make the code messy and hard to read. Keeping words in a separate file also means we can easily add or remove words without changing any logic.

---
## Authors
Andres Elizondo & Sabrina Ramirez Libertella
GitHub: @aelhin07 @SabrinaRLiber
Hult International Business School — SUM1 2026

---
## Acknowledgements
This project was built as the CS50P Final Project. Claude and ChatGPT were used as coding assistants whenever we ran into a problem or got stuck, helping us debug and think through solutions. ChatGPT was also used to help generate the list of common 5-letter words in words.txt. Oscar Elizondo helped test the game by playing through multiple rounds and checking that the color feedback and edge cases worked correctly. All code, design decisions, and understanding of the implementation are our own.