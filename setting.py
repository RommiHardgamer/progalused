import pygame

class Settings:
    """A class to store all settings for Bubble Bluster."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 139)
        self.caption = 'Bubble Bluster'
        
        self.bubble_min_r = 10
        self.bubble_min_r = 50

pygame.init()
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption(settings.caption)

# Start the main loop for the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background.
    screen.fill(settings.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

pygame.quit()