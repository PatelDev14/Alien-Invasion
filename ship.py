import pygame

class Ship:

    def __init__(self, ai_game):
        """Initializing the ship and setting its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #rect here means a rectangle.

        self.image = pygame.image.load('images/ship.bmp') #Getting the image of the ship.
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom #Starting the ship at the bottom centere of the screen.

        #Movement Flag.
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x) #Storing a decimal value for the ships horizontal position.

    def update(self):
        """Updating the ships position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x  =self.x #Updating the rect object from self.x.



    def blitme(self):
        """Drawing the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centering the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        

