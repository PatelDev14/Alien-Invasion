import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing the single alien."""
    def __init__(self, ai_game):
        """Initializing the alien and setting its starting position"""

        super().__init__()
        self.screen = ai_game.screen

        self.settings = ai_game.settings

        #Loading the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Starting rach new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) #Storing a decimal value for the aliens horizontal position.

    def update(self):
        """Moving the alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returning True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

        
    

