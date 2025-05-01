import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class that managers the bullets fired from the ship."""

    def __init__(self, ai_game):
        """A bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
    
        # Storing the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet up the screen."""
        #Updating the position of the bullet.
        self.y -= self.settings.bullet_speed
        # Updating the position of the bullet.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Drawing the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

        