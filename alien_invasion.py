import sys #This contains tools to exit the game when the player quits the game.
import pygame #This module contains the functionality we need to make a game.

from settings import Settings #This imports the settings module which contains the settings for the game.

class AlienInvasion: #This is the main class for the game.
    """Main Class for managing game assets and behavior."""

    def __init__(self): 
        """Initializing the game and creating resources"""

        pygame.init() #This function initializes the background setting that Pygame needs to work.
        self.settings= Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.scrren_height))#Display screen size(tuple wide, high).
        pygame.display.set_caption("Alien Invasion") 
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the main loop for the game."""
        while True:
            for event in pygame.event.get():#Event is the action that user perform while playing the game, such as pressing the key or moving the mouse.
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color) #This fills the screen with the background color.

            pygame.display.flip()#This makes the most recently drawn screen visible.

if __name__ == '__main__':
    # Creating an instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()