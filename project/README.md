# Terminal Wordle
#### Video Demo: https://www.youtube.com/watch?v=r1nXAF07jLI
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
This is the main file of the project. It contains all the game logic. It has the `main()` function and five other functions. Each function has its own job.

### `load_word_list(filepath)`
This function opens the `words.txt` file and reads each line. It creates a list of valid 5-letter words. It also changes every word to uppercase so the program can compare the words correctly. If the file is not found or has no valid words, the program shows an error message and stops. We keep the words in a separate file because it is easier to update. We can add or remove words without changing the Python code.

### `get_random_word(word_list)`
This function takes the word list and chooses one random word using Python’s `random.choice()` function. Before choosing a word, it checks if the list is empty. If the list is empty, it raises a `ValueError`. We made this a separate function to keep the code simple and make it easier to test.

### `check_guess(guess, target)`
This is the most important function in the game. It compares the player’s guess with the secret word. It returns a list of tuples. Each tuple has a letter and its result: `"correct"`, `"present"`, or `"absent"`. The function uses a two-pass method to handle repeated letters correctly. In the first pass, it checks which letters are in the correct position. In the second pass, it checks if the other letters are somewhere else in the word. This stops repeated letters from being counted more than once. It also follows the real Wordle rules.

### `is_valid_word(word, word_list)`
This function checks if the player’s guess is valid.
It checks that the word:
* Has exactly 5 characters
* Only contains letters
* Is inside the word list
It also removes extra spaces before checking the word. If the word is not valid, the function returns `False`, and the player must enter another word.

### `format_feedback(result)`
This function takes the result from `check_guess` and changes it into a colored string for the terminal. It uses the `colorama` library to give each letter a green, yellow, or white background. The color depends on whether the letter is correct, present, or absent. We kept this function separate from `check_guess` because they have different jobs. `check_guess` checks the game logic, while `format_feedback` shows the result on the screen. This keeps the code clean and easy to understand.

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
### Why we used Colorama
We wanted the game to show colors like the real Wordle game. We used Colorama because it is easy to use and works on Windows and Mac. Without Colorama, the color codes may appear as strange letters or symbols instead of colors.

### Why we used a two-pass algorithm
At first, we used a single-pass method in the `check_guess` function. But when we tested words with repeated letters, the results were sometimes wrong. For example, if the answer is `STONE` and the guess is `SCENE`, the answer only has one `E`. A single-pass method could mark both `E`s as correct or present. To fix this, we used a two-pass method. First, the function checks the letters that are in the correct position. Then, it checks the other letters. This helps the game handle repeated letters correctly.

### Why we kept the functions small and separate
We wanted each function to have one clear job. For example, `check_guess` checks the letters, `format_feedback` shows the colors, and `is_valid_word` checks if the guess is valid. This also made testing easier. We could test each function by itself and find problems faster.

### Why we loaded the words from a file
Putting hundreds of words inside the Python code would make it messy and hard to read. Using a separate file keeps the code clean. It also makes it easy to add or remove words without changing the game logic.

---
## Authors
Andres Elizondo & Sabrina Ramirez Libertella
GitHub: @aelhin07 @SabrinaRLiber
Hult International Business School — SUM1 2026

---
## Acknowledgements
This project was created for the CS50P Final Project. We used Claude and ChatGPT as coding assistants when we had problems or got stuck. They helped us find bugs and think of possible solutions. ChatGPT was also used to help create the list of common 5-letter words in the `words.txt` file. Oscar Elizondo helped test the game by playing several rounds. He checked that the colors worked correctly and that the game handled different cases properly. All the code, design choices, and understanding of how the project works are our own.