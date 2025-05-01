import sys #This contains tools to exit the game when the player quits the game.
import pygame #This module contains the functionality we need to make a game.

from settings import Settings #This imports the settings module which contains the settings for the game.
from ship import Ship #This imports the ship module which contains the ship class.
from bullet import Bullet #This imports the bullet module which contains the bullet class.

class AlienInvasion: #This is the main class for the game.
    """Main Class for managing game assets and behavior."""

    def __init__(self): 
        """Initializing the game and creating resources"""

        pygame.init() #This function initializes the background setting that Pygame needs to work.
        self.settings= Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #This creates a screen for the game.
        self.settings.screen_width = self.screen.get_rect().width #This gets the width of the screen.
        self.settings.screen_height = self.screen.get_rect().height #This gets the height of the screen.
        pygame.display.set_caption("Alien Invasion") 
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Starting the main loop for the game."""
        while True:
            self._check_events() #This function checks for events that occur in the game.
            self.ship.update()
            self.bullets.update()

            #Getting rid of the bullets, they leave the screen but keep growing in the y-coordinate and cosume memory.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))#This prints the number of bullets on the screen.
            
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
                    self._check_keydown_events(event)
                    

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left  = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left  = False

    def _fire_bullet(self):
        """Creating a new bullet and adding it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_screen(self):
        """Updating the screen and drawing the ship."""
        #This function updates the screen with the most recent screen.
        #It also draws the ship at its current location.
        self.screen.fill(self.settings.bg_color) #This fills the screen with the background color.
        self.ship.blitme() #This draws the ship at its current location.

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()#This makes the most recently drawn screen visible.

if __name__ == '__main__':
    # Creating an instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()