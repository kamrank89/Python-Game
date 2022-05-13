import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting posisiont."""
        self.screen = ai_game.screen
        self.screen_width = ai_game.settings.screen_width
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.width = self.image.get_rect().size[0]
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.shooting = False

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            if self.x >= self.screen_width - self.width:
                self.moving_right = False
            else:
                self.x += self.settings.move_speed
        elif self.moving_left:
            if self.x <= 0:
                self.moving_left = False
            else:
                self.x -= self.settings.move_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)