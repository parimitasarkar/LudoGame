import pygame
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BOARD_SIZE = 500
BOARD_POS = ((WINDOW_WIDTH - BOARD_SIZE) // 2, (WINDOW_HEIGHT - BOARD_SIZE) // 2)
PLAYER_SIZE = 20
PLAYER_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
DICE_SIZE = 40
FONT_SIZE = 24
PLAYER_NAMES = ["Player 1", "Player 2", "Player 3", "Player 4"]

class LudoGame:
    def __init__(self):
        self.players = [{"name": name, "position": 0} for name in PLAYER_NAMES]
        self.current_player = 0
        self.dice_value = 0

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)

    def move_player(self, steps):
        player = self.players[self.current_player]
        player["position"] += steps
        if player["position"] > 100:
            player["position"] -= steps

    def switch_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def is_winner(self):
        return any(player["position"] >= 100 for player in self.players)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ludo Game")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Main game loop
game = LudoGame()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game.is_winner():
            if event.button == 1:
                game.roll_dice()
                game.move_player(game.dice_value)
                game.switch_player()

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw the game board
    pygame.draw.rect(window, (0, 0, 0), (BOARD_POS[0], BOARD_POS[1], BOARD_SIZE, BOARD_SIZE))

    # Draw players
    for i, player in enumerate(game.players):
        x = BOARD_POS[0] + (player["position"] % 10) * (BOARD_SIZE // 10) + (BOARD_SIZE // 20) - PLAYER_SIZE // 2
        y = BOARD_POS[1] + (player["position"] // 10) * (BOARD_SIZE // 10) + (BOARD_SIZE // 20) - PLAYER_SIZE // 2
        pygame.draw.circle(window, PLAYER_COLORS[i], (x, y), PLAYER_SIZE)

    # Draw the dice
    dice_text = font.render(f"Dice: {game.dice_value}", True, (0, 0, 0))
    window.blit(dice_text, (BOARD_POS[0], BOARD_POS[1] - 50))

    # Draw current player
    current_player_text = font.render(f"Current Player: {game.players[game.current_player]['name']}", True, (0, 0, 0))
    window.blit(current_player_text, (BOARD_POS[0], BOARD_POS[1] - 100))

    # Check for winner
    if game.is_winner():
        winner_text = font.render(f"Winner: {game.players[game.current_player]['name']}", True, (255, 0, 0))
        window.blit(winner_text, (WINDOW_WIDTH // 2 - 100, BOARD_POS[1] + BOARD_SIZE + 50))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
