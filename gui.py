import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 800
BOARD_ROWS, BOARD_COLS = 8, 8
SQUARE_SIZE = WIDTH // BOARD_COLS
PIECE_RADIUS = SQUARE_SIZE // 2 - 2

# Colors
DARK_GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
HIGHLIGHT_COLOR = (0, 255, 0)

class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Othello")
        self.font = pygame.font.Font(None, 30)
        self.clock = pygame.time.Clock()

    def draw_board(self):
        self.screen.fill(DARK_GREEN)
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
                pygame.draw.circle(self.screen, BLACK, rect.center, PIECE_RADIUS, 1)

    def draw_pieces(self, board):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                if board[row * BOARD_COLS + col] == 1:
                    self.draw_piece(center, BLACK)
                elif board[row * BOARD_COLS + col] == -1:
                    self.draw_piece(center, WHITE)

    def draw_piece(self, center, color):
        x, y = center
        # Draw main circle (black or white)
        pygame.draw.circle(self.screen, color, (x, y), PIECE_RADIUS)
        # Draw gray top
        pygame.draw.circle(self.screen, GRAY, (x, y - PIECE_RADIUS // 2), PIECE_RADIUS)
        # Draw outline
        pygame.draw.circle(self.screen, BLACK, (x, y), PIECE_RADIUS, 1)

    def highlight_legal_moves(self, legal_moves):
        for move in legal_moves:
            row, col = divmod(move, BOARD_COLS)
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(self.screen, HIGHLIGHT_COLOR, center, PIECE_RADIUS, 2)
            text = self.font.render("1", True, HIGHLIGHT_COLOR)
            text_rect = text.get_rect(center=center)
            self.screen.blit(text, text_rect)

    def update_board(self, board, legal_moves=None):
        self.draw_board()
        self.draw_pieces(board)
        if legal_moves:
            self.highlight_legal_moves(legal_moves)
        pygame.display.update()

    def get_clicked_position(self, mouse_pos):
        x, y = mouse_pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row * BOARD_COLS + col

    def run_event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return self.get_clicked_position(event.pos)
        return None

    def show_winner(self, winner):
        if winner == 1:
            text = "Black Wins!"
        elif winner == -1:
            text = "White Wins!"
        else:
            text = "It's a Draw!"
        
        winner_text = self.font.render(text, True, WHITE)
        text_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(winner_text, text_rect)
        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(30)