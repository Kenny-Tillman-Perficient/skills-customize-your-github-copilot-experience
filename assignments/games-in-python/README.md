
# 📘 Assignment: Games in Python - Hangman

## 🎯 Objective

Build a Hangman word-guessing game using Python strings, loops, conditionals, and user input. Practice tracking game state and responding to player guesses.

## 📝 Tasks

### 🛠️ Set Up the Game and Reveal the Word

#### Description
Use the provided word list to choose a secret word, then let the player guess letters and reveal the matching letters.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Start with no guessed letters and display each unrevealed letter as an underscore.
- Ask the player for one letter at a time and update the displayed word after each guess.
- Continue until every letter in the secret word has been guessed or the player runs out of attempts.

### 🛠️ Track Attempts and Finish the Game

#### Description
Track incorrect guesses and end the game with a clear message for the player.

#### Requirements
Completed program should:

- Set a maximum of 6 incorrect guesses and decrease the remaining attempts when a guess is not in the secret word.
- Display the number of incorrect guesses remaining after each incorrect guess.
- End with a win message when the player reveals the whole word.
- End with a loss message and reveal the secret word when no attempts remain.
