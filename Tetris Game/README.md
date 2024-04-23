# Tetris Game

This is a Tetris game implementation using Python and the Pygame library. The game features classic Tetris gameplay, where the player must arrange falling tetromino shapes to form complete rows, which then disappear, earning points. The game includes a start screen, a "How to Play" screen, and a score and record tracking system.

![image](https://github.com/mirelesDavid/mirelesDavid-Projects/assets/141588489/3779103d-b43c-4136-bc8b-fd0f8fd2435b)


## Features

- Classic Tetris gameplay
- Start screen with background video
- "How to Play" screen
- Score and personal record tracking
- Next tetromino preview
- Background music and sound effects
- Game over detection and restart

![image](https://github.com/mirelesDavid/mirelesDavid-Projects/assets/141588489/986539b3-f157-4425-95ed-c662b5957021)


## Technologies Used

- Python
- Pygame
- MoviePy (for playing the background video on the start screen)

## Project Structure

The project consists of a single Python file `tetris.py` that contains all the game logic and functionality. Additionally, it uses the following directories and files:

- `img/`: Directory containing images used in the game, such as backgrounds and the "How to Play" image.
- `music/`: Directory containing music files for the game's background music and start screen.
- `font/`: Directory containing the font file used for rendering text in the game.
- `record`: File for storing the player's personal record (high score).

## Getting Started

1. Make sure you have Python and the required libraries (Pygame, MoviePy) installed on your machine.
2. Clone the repository or download the project files.
3. Navigate to the project directory.
4. Run the `tetris.py` file using Python: `python tetris.py`.

## Gameplay

1. On the start screen, press "Enter" to start the game, "Q" to quit, or "H" to view the "How to Play" screen.
2. Use the left and right arrow keys to move the tetromino horizontally.
3. Use the down arrow key to increase the falling speed of the tetromino.
4. Use the up arrow key to rotate the tetromino clockwise.
5. Use the "Z" key to rotate the tetromino counter-clockwise.
6. Use the spacebar to make the tetromino fall instantly.
7. When a row is completed, it disappears, and you earn points based on the number of rows cleared simultaneously.
8. The game ends when the tetrominos reach the top of the playing field.
9. Your personal record (high score) is displayed and updated if you surpass your previous record.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
