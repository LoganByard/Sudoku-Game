import random
from random import shuffle

class sudoku_board:
    """
    Class representing the sudoku game board and its logic including baord generation,
    validating moves, and managing the state of the board
    """
    def __init__(self):
        """
        Initialize the sudoku board. This function creates a 9x9 board and it up with the
        easy difficulty
        """
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.solution = None
        self.generate_solution()
        self.set_difficulty("easy")

    def generate_solution(self):
        """
        Generates a complete valid board. Begins by filling in the 3x3 boxes along the diagonal
        """

        for i in [0, 3, 6]:
            self.fill_3x3_box(i, i)
        self.fill_remaining_cells(0, 3)
        self.solution = [row[:] for row in self.board]

    def set_difficulty(self, difficulty):
        """
        Sets the difficulty of the game by removing numbers from the solution
        """

        self.board = [row[:] for row in self.solution]
        cells_to_remove = {
            "easy": 30,
            "medium": 45,
            "hard": 55
        }
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)
        for i, j in positions[:cells_to_remove[difficulty]]:
            self.board[i][j] = 0

    def fill_3x3_box(self, row_start, col_start):
        """
        Fills a 3x3 box with random numbers 1-9
        """

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        index = 0
        for row in [row_start, row_start + 1, row_start + 2]:
            for col in [col_start, col_start + 1, col_start + 2]:
                self.board[row][col] = numbers[index]
                index += 1

    def fill_remaining_cells(self, row, col):
        """
         Fills the remaining empty spaces by using backtracking algorithm
         :return true if the board was successfully filled
        """

        # Base case (returns true if entire board filled)
        if row == 9:
            return True
        # Move to next row
        if col == 9:
            return self.fill_remaining_cells(row + 1, 0)
        # If cell is already filled skip it
        if self.board[row][col] != 0:
            return self.fill_remaining_cells(row, col + 1)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(numbers)

        # Try each number in the shuffled list
        for num in numbers:
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                # Recursively try to fill the rest of the board
                if self.fill_remaining_cells(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def is_valid(self, row, col, num):
        """
        Checks if a number can be placed in the specified position
        """
        # Check the entire row and column for conflicts
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        # Check 3x3 box for conflicts
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True

    def check_solution(self, row, col, num):
        """
        Checks if a number matches the solution in the specified box
        """
        return self.solution[row][col] == num

    def place_number(self, row, col, num):
        """
        Places a number on the board if it matches the solution
        """
        if self.check_solution(row, col, num):
            self.board[row][col] = num
            return True
        return False

    def is_completed(self):
        """
        Checks if the current board matches the entire solution
        """

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.solution[i][j]:
                    return False
        return True

    def get_board(self):
        """
        gets the current sudoku board
        """
        return self.board

    def is_cell_empty(self, row, col):
        """
        Checks if a cell is empty or not
        """
        return self.board[row][col] == 0 or self.board[row][col] != self.solution[row][col]