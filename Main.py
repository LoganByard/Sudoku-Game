import pygame
from constants import screen
from sudoku_board import sudoku_board
from gui import SudokuGUI

def main():
    board = sudoku_board()
    game = SudokuGUI(board)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                game.handle_key(event.key)

        game.draw_board()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()