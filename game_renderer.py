import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
BOARD_SIZE = 19
CELL_SIZE = 40
BORDER_SIZE = 20
STONE_RADIUS = CELL_SIZE // 2 - 4
BOARD_COLOR = (222, 184, 135)  # Light brown for the Go board
LINE_COLOR = (0, 0, 0)  # Black lines
BLACK_STONE_COLOR = (0, 0, 0)
WHITE_STONE_COLOR = (255, 255, 255)
WINDOW_SIZE = BOARD_SIZE * CELL_SIZE + 2 * BORDER_SIZE

# Set up display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Go Game Renderer")

# Function to draw the Go board
def draw_board():
    screen.fill(BOARD_COLOR)

    # Draw grid lines
    for i in range(BOARD_SIZE):
        x = BORDER_SIZE + i * CELL_SIZE
        y = BORDER_SIZE + i * CELL_SIZE
        pygame.draw.line(screen, LINE_COLOR, (x, BORDER_SIZE), (x, WINDOW_SIZE - BORDER_SIZE), 1)
        pygame.draw.line(screen, LINE_COLOR, (BORDER_SIZE, y), (WINDOW_SIZE - BORDER_SIZE, y), 1)

# Function to draw stones
def draw_stones(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = BORDER_SIZE + col * CELL_SIZE
            y = BORDER_SIZE + row * CELL_SIZE
            if board[row, col] == -1:  # Black stone
                pygame.draw.circle(screen, BLACK_STONE_COLOR, (x, y), STONE_RADIUS)
            elif board[row, col] == 1:  # White stone
                pygame.draw.circle(screen, WHITE_STONE_COLOR, (x, y), STONE_RADIUS)
                pygame.draw.circle(screen, LINE_COLOR, (x, y), STONE_RADIUS, 1)  # Outline for contrast

# Main function
def main():
    # Example board state
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    board[3, 3] = -1  # Black stone
    board[3, 15] = 1  # White stone

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the board and stones
        draw_board()
        draw_stones(board)

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
