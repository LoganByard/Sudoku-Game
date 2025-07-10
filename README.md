# Sudoku Game (Python + Pygame)

This is a fully playable Sudoku game implemented in Python using Pygame. The game features a complete board generator, difficulty settings, real-time validation, note-taking mode, keyboard/mouse input handling, and win/loss detection.

---

## Features

- **Playable GUI**: Fully interactive interface using Pygame with clickable cells, number pad, and live updates.
- **Difficulty Levels**: Choose from Easy, Medium, or Hard, with different numbers of pre-filled cells.
- **Board Generator**: Random Sudoku board generator using backtracking algorithm for valid puzzle generation.
- **Validation**: Real-time checking of player inputs against the solution.
- **Note Mode**: Toggle note mode to input small hints in each cell.
- **Game Logic**: Win/loss conditions enforced with a maximum mistake limit.

---

## Screenshots

<img width="792" height="623" alt="image" src="https://github.com/user-attachments/assets/d86ba1aa-46e0-4e61-9d1e-427cf4cb8dd0" />


---

## Technologies Used

- **Language**: Python 3
- **Library**: Pygame
- **Concepts**: Backtracking algorithm, OOP, 2D array manipulation, GUI event handling

---

## File Structure

```
.
├── main.py              # Entry point for launching the game
├── sudoku_board.py      # Handles board generation and solution logic
├── gui.py               # Pygame-based GUI rendering and game logic
├── constants.py         # Color definitions and screen setup
```

---

## Getting Started

### Prerequisites

Make sure Python 3 and `pygame` are installed:

```bash
pip install pygame
```

### Run the Game

```bash
python main.py
```

---

## Controls

- **Mouse Click**: Select cell or number from numpad
- **Keyboard Arrows**: Navigate between cells
- **1-9 Keys**: Input number into selected cell
- **N Key**: Toggle note mode

---

## Future Improvements

- Add a timer-based scoring system
- Include animations or sound effects
- Add save/load game state
- Expand to include mobile/touch support

---

## License

This project is for educational and portfolio purposes.

---

## Contact

Created by [Logan Byard](https://github.com/LoganByard). Feel free to reach out via GitHub Issues for suggestions or contributions.
