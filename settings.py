class Settings():
    """A class to store all the settings for alien invasion"""

    def __init__(self):
        """initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = 0, 0, 0
        self.bullets_allowed = 3


