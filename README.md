# TicTacToe (Python Game)

A simple TicTacToe game built with Python, using classes and functions. The code is documented to make it easier to understand.

## How Does the Game Work?

It's TicTacToe! Never played it before? No problem, I've got you!

The goal is to be the first player to align three X's or O's in a row. You can do this horizontally, vertically, or diagonally.

If all spaces are filled and nobody manages to align three symbols, the game ends in a draw. No points are awarded, and the board resets for the next round.

## About the Code

I used a class to handle the console interface and tried to keep things as clean and readable as possible. I also experimented with list comprehensions and one-liners to make some parts of the code more concise.

The game currently has two modes:

 * **PvP (Player vs. Player)**: Play against another person.

 * **PvE (Player vs. Environment)**: Play against the computer.

The computer doesn't have any AI yet, but I'm planning to implement one in the future! For now, it simply places an "O" in a random available position, so it's pretty easy to beat. 

There are also two game modes:

 * **One Shot**: The first player to win takes the game.

 * **3 Rounds**: A best-of-three format. The first player to win two rounds takes the game. Draws don't count toward the round limit, so if the score is 1-1, there's one final round to decide the winner.

## Final Thoughts

This was a fun project to create and a great exercise to refresh my programming logic and Python skills!

More improvements and projects coming soon!
