# Portfolio Assignment from Analysis of Algorithms (Dec 2020)
My portfolio/final project from my Analysis of Algorithms (CS 325) class. Not edited since it was submitted in December 2020. I received a perfect score on it.

## Assignment Instructions:

- Choose one of the 24 puzzles in the PDF (not included in this repository) or create your own puzzle!
- Use the most appropriate algorithm method from our course to solve the decision problem in the paper. (You only are required one algorithm that verifies the players solution is viable against the possible puzzle instances). Players should be able to enter their own attempt at a solution. 
- Create the code for that game as well as a brief description of the rules and a reference to its time complexity. A GUI playable game is not required, but you are welcome to do so. Pygame is a good choice for this in Python. 
- You will also need to prove a summarization of your solution to show proof of your method usage, that you will include in your PDF.
- Prove your algorithm used for the decision of the problem from the paper rather than trying to prove your game or puzzle of choice. You want to prove the solution either is or is not NP Complete

## Information About My Project:
#### To play the Sudoku game, run sudoku.py and follow the printed instructions in the terminal. 

1. It will print the game rules and instructions as follows:

Game Rules: The 9x9 board is divided into 9 larger squares (each with 9 squares inside). 
The goal is to get the numbers 1-9 in each big square. 
Each number can only appear once in a row, column, or big square.

Playing Instructions: 
Use the letters on the left and numbers on the top of the board to see the names 
of the squares (Ex: A6, G2, etc.). To enter a number into a square, you enter 
the square name and the number you wish to put there, separated by a space. 
For example, 'A4 3' would put a '3' in spot 'A4'. To make the spot empty again,
just put an underscore in place of a number: 'A4 _'

2. Then it will ask you to select a difficulty level (easy, medium, hard). 
You can also enter 'test' to print a correctly filled out full board.

3. After entering the difficulty level, your puzzle will be printed, along with:
Reminder: Enter 'q' to quit, 'submit' when done, 'solution' to give up and
 see the fully solved board, or 'help' to see the instructions again.
 Enter the square name and number:
 
4. After entering a square name and number, it will update and print the board again,
 print the reminder message, and ask for another square name and number. This process
 will continue until you enter 'q', 'submit', or 'solution' (as seen in reminder message).
