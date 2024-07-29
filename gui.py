import numpy as np
import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS = 8
BOARD_COLS = 8
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)


class GUI:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Set up the display
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Othello")
        self.screen.fill(BG_COLOR)

    def draw_lines(self):
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        for col in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.display.update()

    def draw_figures(self, board):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row * BOARD_COLS + col] == 1:
                    pygame.draw.circle(self.screen, BLACK_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif board[row * BOARD_COLS + col] == -1:
                    pygame.draw.circle(self.screen, WHITE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
        pygame.display.update()

    def update_board(self, board):
        self.screen.fill(BG_COLOR)
        self.draw_lines()
        self.draw_figures(board)


# # Test the GUI
# gui = GUI()
# gui.draw_lines()

# # Run the game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()