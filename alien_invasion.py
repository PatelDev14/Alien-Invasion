import sys #This contains tools to exit the game when the player quits the game.
import pygame #This module contains the functionality we need to make a game.

from settings import Settings #This imports the settings module which contains the settings for the game.
from ship import Ship #This imports the ship module which contains the ship class.

class AlienInvasion: #This is the main class for the game.
    """Main Class for managing game assets and behavior."""

    def __init__(self): 
        """Initializing the game and creating resources"""

        pygame.init() #This function initializes the background setting that Pygame needs to work.
        self.settings= Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#Display screen size(tuple wide, high).
        pygame.display.set_caption("Alien Invasion") 
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)

    def run_game(self):
        """Starting the main loop for the game."""
        while True:
            self._check_events() #This function checks for events that occur in the game.
            self.ship.update()
            self._update_screen() #This function updates the screen with the most recent screen.

    def _check_events(self):
        """Responding to keypresses and mouse events."""
        #This function checks for events that occur in the game.
        #It checks for events such as pressing the key or moving the mouse.
        #It also checks for the quit event which is when the player quits the game.
        for event in pygame.event.get():#Event is the action that user perform while playing the game, such as pressing the key or moving the mouse.
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key ==pygame.K_LEFT:
                        self.ship.moving_left  = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left  = False


    def _update_screen(self):
        """Updating the screen and drawing the ship."""
        #This function updates the screen with the most recent screen.
        #It also draws the ship at its current location.
        self.screen.fill(self.settings.bg_color) #This fills the screen with the background color.
        self.ship.blitme() #This draws the ship at its current location.

        pygame.display.flip()#This makes the most recently drawn screen visible.

if __name__ == '__main__':
    # Creating an instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()