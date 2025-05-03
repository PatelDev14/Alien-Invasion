class GameStats:
    """Tracking statistics for the game."""

    def __init__(self, ai_game):
        """Initializing statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

       
    def reset_stats(self):
        """Initializing the statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit


