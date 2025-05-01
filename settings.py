class Settings:
    """A class to manage settings for the application."""
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        #Bullets
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 #This is the number of bullets that can be fired at once.