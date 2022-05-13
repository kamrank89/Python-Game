class GameStats:
    '''Track statistics fpr Alien Invasion'''
    def __init__(self, ai_game):
        """Initialized statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialized statistics that can change during the game."""
        self.ship_left = self.settings.ship_left
