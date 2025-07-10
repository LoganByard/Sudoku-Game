import pygame
import time
from constants import *

class SudokuGUI:
    """
    Class for building the gui and handling user interaction with the game
    """
    def __init__(self, board):
        """
        Initialize the default game settings
        """
        self.backend = board
        self.board = board.get_board()
        self.selected = None
        self.current_time = 0
        self.start_time = time.time()
        self.mistakes = 0
        self.notes = [[set() for i in range(9)] for i in range(9)]
        self.note_mode = False
        self.difficulty = "easy"
        self.game_over = False
        self.game_won = False
        self.wrong_cells = set()

    def draw_board(self):
        """
        Draw the main sudoku board and all of its components
        """

        # Set the screen to a white background
        screen.fill(WHITE)
        cell_size = 50
        start_x = 50
        start_y = 50

        # Draw the highlighting for celected box, row, and column
        if self.selected and not self.game_over and not self.game_won:
            row, col = self.selected
            # Highlights the row and column
            pygame.draw.rect(screen, LIGHT_BLUE, (start_x + col * cell_size, start_y, cell_size, 450))
            pygame.draw.rect(screen, LIGHT_BLUE, (start_x, start_y + row * cell_size, 450, cell_size))

            # Highlights the 3x3 box
            box_x = (col // 3) * 3
            box_y = (row // 3) * 3
            pygame.draw.rect(screen, LIGHT_BLUE,
                             (start_x + box_x * cell_size, start_y + box_y * cell_size, cell_size * 3, cell_size * 3))

            # Highlight the selected box with darker blue
            pygame.draw.rect(screen, DARKER_BLUE,
                             (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

        # Draw the lines of the grid
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(screen, BLACK, (start_x + i * cell_size, start_y),
                             (start_x + i * cell_size, start_y + 450), line_width)
            pygame.draw.line(screen, BLACK, (start_x, start_y + i * cell_size),
                             (start_x + 450, start_y + i * cell_size), line_width)

        # Draw numbers and notes
        font = pygame.font.Font(None, 36)
        small_font = pygame.font.Font(None, 20)

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    #SHow the numbers in red if they're wrong, or black if correct
                    color = RED if (i, j) in self.wrong_cells else BLACK
                    text = font.render(str(self.board[i][j]), True, color)
                    screen.blit(text, (start_x + j * cell_size + 15, start_y + i * cell_size + 15))
                elif self.notes[i][j]:
                    # Draw the note numbers
                    for num in self.notes[i][j]:
                        note_text = small_font.render(str(num), True, GRAY)
                        x_offset = ((num - 1) % 3) * 15
                        y_offset = ((num - 1) // 3) * 15
                        screen.blit(note_text,
                                    (start_x + j * cell_size + 5 + x_offset, start_y + i * cell_size + 5 + y_offset))

        self.draw_numpad()
        self.draw_ui()

        if self.game_over:
            self.draw_game_over()
        elif self.game_won:
            self.draw_game_won()

    def draw_game_over(self):
        """
        Draws the game over state when a player loses
        """
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(128)
        overlay.fill(WHITE)
        screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 74)
        text = font.render("Game Over!", True, RED)
        text_rect = text.get_rect(center=(400, 250))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        play_again = font.render("Play Again", True, BLACK)
        pygame.draw.rect(screen, BLACK, (350, 350, 100, 40), 1)
        text_rect = play_again.get_rect(center=(400, 370))
        screen.blit(play_again, text_rect)

    def draw_game_won(self):
        """
        Draws the game won state when a player wins
        """
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(128)
        overlay.fill(WHITE)
        screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 74)
        text = font.render("You Win!", True, BLUE)
        text_rect = text.get_rect(center=(400, 250))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        play_again = font.render("Play Again", True, BLACK)
        pygame.draw.rect(screen, BLACK, (350, 350, 100, 40), 1)
        text_rect = play_again.get_rect(center=(400, 370))
        screen.blit(play_again, text_rect)

    def draw_numpad(self):
        """
        Draws the on screen numpad
        """
        start_x = 550
        start_y = 50
        size = 40
        font = pygame.font.Font(None, 36)

        for i in range(9):
            row = i // 3
            col = i % 3
            pygame.draw.rect(screen, BLACK, (start_x + col * size, start_y + row * size, size, size), 1)
            text = font.render(str(i + 1), True, BLACK)
            screen.blit(text, (start_x + col * size + 15, start_y + row * size + 10))

    def draw_ui(self):
        """
        Draws the timer, mistakes, and difficulty buttons
        """
        font = pygame.font.Font(None, 36)
        bold_font = pygame.font.Font(None, 40)
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        time_text = font.render(f"Time: {minutes:02d}:{seconds:02d}", True, BLACK)
        screen.blit(time_text, (550, 200))

        mistakes_text = font.render(f"Mistakes: {self.mistakes}/3", True, BLACK)
        screen.blit(mistakes_text, (550, 250))

        note_text = font.render("Notes: " + ("On" if self.note_mode else "Off"), True, BLACK)
        screen.blit(note_text, (550, 300))

        difficulty_buttons = ["Easy", "Medium", "Hard"]
        for i, diff in enumerate(difficulty_buttons):
            pygame.draw.rect(screen, BLACK, (550, 350 + i * 50, 100, 40), 1)
            if diff.lower() == self.difficulty:
                text = bold_font.render(diff, True, BLACK)
            else:
                text = font.render(diff, True, BLACK)
            screen.blit(text, (560, 360 + i * 50))

    def handle_click(self, pos):
        """
        Handles when the user clicks the game
        """

        # Handles when the player clicks during the game over/game won message
        if self.game_over or self.game_won:
            if 350 <= pos[0] <= 450 and 350 <= pos[1] <= 390:
                self.reset_game()
                self.backend.set_difficulty(self.difficulty)
                self.board = self.backend.get_board()
            return

        # Handles selecting a box in the sudoku board
        cell_size = 50
        start_x = 50
        start_y = 50

        if start_x <= pos[0] <= start_x + 450 and start_y <= pos[1] <= start_y + 450:
            row = (pos[1] - start_y) // cell_size
            col = (pos[0] - start_x) // cell_size
            if self.backend.is_cell_empty(row, col) or (row, col) in self.wrong_cells:
                self.selected = (row, col)

        # Handles when the click is on the numpad
        numpad_x = 550
        numpad_y = 50
        size = 40
        if numpad_x <= pos[0] <= numpad_x + 3 * size and numpad_y <= pos[1] <= numpad_y + 3 * size:
            col = (pos[0] - numpad_x) // size
            row = (pos[1] - numpad_y) // size
            num = row * 3 + col + 1
            if self.selected:
                self.handle_number_input(num)

        if 550 <= pos[0] <= 650:
            if 300 <= pos[1] <= 330: # Notes on/off
                self.note_mode = not self.note_mode
            # Handle difficulty selection buttons
            elif 350 <= pos[1] <= 390:
                self.difficulty = "easy"
                self.backend.set_difficulty("easy")
                self.board = self.backend.get_board()
                self.reset_game()
            elif 400 <= pos[1] <= 440:
                self.difficulty = "medium"
                self.backend.set_difficulty("medium")
                self.board = self.backend.get_board()
                self.reset_game()
            elif 450 <= pos[1] <= 490:
                self.difficulty = "hard"
                self.backend.set_difficulty("hard")
                self.board = self.backend.get_board()
                self.reset_game()

    def reset_game(self):
        """
        Resets the game to the original state
        """
        self.mistakes = 0
        self.start_time = time.time()
        self.notes = [[set() for i in range(9)] for i in range(9)]
        self.selected = None
        self.game_over = False
        self.game_won = False
        self.wrong_cells = set()

    def handle_number_input(self, num):
        """
        Handles the user inputting numbers from the keyboard or the num pad
        """
        if not self.selected or self.game_over or self.game_won:
            return

        row, col = self.selected
        if self.backend.is_cell_empty(row, col) or (row, col) in self.wrong_cells:
            if self.note_mode:
                if num in self.notes[row][col]:
                    self.notes[row][col].remove(num)
                else:
                    self.notes[row][col].add(num)
            else:
                if self.backend.check_solution(row, col, num):
                    # Correct number placement
                    self.backend.place_number(row, col, num)
                    self.board[row][col] = num
                    if (row, col) in self.wrong_cells:
                        self.wrong_cells.remove((row, col))
                    if self.backend.is_completed():
                        self.game_won = True
                else: # Wrong number placement
                    self.mistakes += 1
                    self.wrong_cells.add((row, col))
                    self.board[row][col] = num
                    if self.mistakes >= 3:
                        self.game_over = True

    def handle_key(self, key):
        """
        Handles when the player uses the keyboard for navigation and entering numbers
        """
        if self.game_over or self.game_won:
            return

        if not self.selected:
            self.selected = (0, 0)
            return

        row, col = self.selected
        if key == pygame.K_UP and row > 0:
            self.selected = (row - 1, col)
        elif key == pygame.K_DOWN and row < 8:
            self.selected = (row + 1, col)
        elif key == pygame.K_LEFT and col > 0:
            self.selected = (row, col - 1)
        elif key == pygame.K_RIGHT and col < 8:
            self.selected = (row, col + 1)
        elif key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                     pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
            num = int(pygame.key.name(key))
            self.handle_number_input(num)
        elif key == pygame.K_n:
            self.note_mode = not self.note_mode