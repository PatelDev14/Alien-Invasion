import sys #This contains tools to exit the game when the player quits the game.
from time import sleep #This module is used to pause the game for a few seconds when the player quits the game.

import pygame #This module contains the functionality we need to make a game.

from settings import Settings #This imports the settings module which contains the settings for the game.
from game_stats import GameStats #This imports the game_stats module which contains the game statistics.
from button import Button #This imports the button module which contains the button class.
from ship import Ship #This imports the ship module which contains the ship class.
from bullet import Bullet #This imports the bullet module which contains the bullet class.

from alien import Alien

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

        #Creating an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play") #This creates a play button for the game.

    def run_game(self):
        """Starting the main loop for the game."""
        while True:
            self._check_events() #This function checks for events that occur in the game.
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_screen() #This function updates the screen with the most recent screen.
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
                    
    def _update_bullets(self):
            self.bullets.update() #This updates the position of the bullets on the screen.
        #Getting rid of the bullets, they leave the screen but keep growing in the y-coordinate and cosume memory.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._check_bulet_alien_collisions()

    def _check_bulet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #Destroying the existing bullets and creating a new fleet.
            self.bullets.empty()
            self._create_fleet()


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

        self.aliens.draw(self.screen) #Drawing the aliens on the screen.

        #Drawing the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()#This makes the most recently drawn screen visible.


    def _create_fleet(self):
        """Creating the fleets of aliens"""
        alien  = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determining the numbe of rows of aliens that can fit on the screen.

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)

        number_rows= available_space_y // (2 * alien_height)

        #Full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Creating an alien and placing it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Updates he position of the aliens."""
        self._check_fleet_edges()
        self.aliens.update()

        #Checking for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom() #Checking if the aliens have reached the bottom of the screen.

    def _check_fleet_edges(self):
        """Responding appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """Dropping the entire fleet and changing the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 #This changes the direction of the fleet.

    
    def _ship_hit(self):
        """Responding to ship being hit by alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1 #Decrementing the number of ships left.

            self.aliens.empty() #Getting rid of the aliens that are on the screen.
            self.bullets.empty()

            self._create_fleet()#Creating new fleet and center of the ship.
            self.ship.center_ship()
            sleep(0.5)#Pausing the game for a few seconds.
        else:
            self.stats.game_active = False


    def _check_aliens_bottom(self):
        """Checking if the aliens have reached the bottom of the screen"""
        screen_rect = slef.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

if __name__ == '__main__':
    # Creating an instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()