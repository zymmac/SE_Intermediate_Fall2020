import sys
import pygame

class EmptyScreen:
    """Blue background for training"""

    def __init__(self):
        """Initialize the screen"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (0,0,255)

    def run_game(self):
        self._check_events()

    def _check_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == "__main__":
    ES = EmptyScreen()
    ES.run_game()