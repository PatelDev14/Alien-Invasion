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
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5 #This is the number of bullets that can be fired at once.

        #Alien settings
        self.alien_speed = 10.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        #1 represents right, -1 represents left.

        self.speedup_scale = 1.1 #This is the speed at which the game speeds up.
        self.score_scale = 1.5 #This is the speed at which the score increases.

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # #Fleet direction of 1 represents right; -1 represents left.
        # self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increasing speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        #Increasing the point value of the aliens.
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)