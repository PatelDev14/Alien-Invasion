class Settings:
    """A class to manage settings for the application."""
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullets
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5 #This is the number of bullets that can be fired at once.

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        #1 represents right, -1 represents left.