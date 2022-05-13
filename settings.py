"""Contains all general settings for Alien Invasion"""
class Settings:
    """Class representing settings for Alien Invasion"""
    def __init__(self):
        """Initialize's Alien Invasion's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.big_color = (240, 240, 240)

        # Ship attributes
        self.move_speed = 1.5
        self.ship_left = 3
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5

        # Fleet direction: 1 = Right // -1 = Left
        self.fleet_direction = 1

        # How quickly game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.move_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings."""
        self.move_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale