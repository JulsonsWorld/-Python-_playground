# Animal Quiz in Python

A simple Python program that quizzes the user on fun animal facts and tracks their score.

## Features

- Asks the player for their name
- Randomizes the order of questions
- Randomizes the order of answer options for each question
- Allows the player to select an answer and updates the score
- Provides real-time feedback on current score

## Implementation / Techniques Used

- **Dictionary (`dict`)** to store questions and answer options with corresponding points
- **List conversion** and **`random.shuffle`** to randomize questions and answers
- **`for` loops** to iterate through questions and answer options
- **`while` loop** for input validation (ensuring answers are 1, 2, or 3)
- **`if` statements** to calculate score based on selected answer
- **Input validation** using `.strip()` to clean player name input
- **Variables** to track player's score and current question
- **User-friendly printing** for clear question and answer display

## Usage Notes

- Run the program in a terminal or command prompt
- Enter your name when prompted
- For each question, type the number of the answer you choose (1, 2, or 3)
- The program displays your current score after each question
- At the end, your total score reflects how many correct answers you selected
