import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    """Initialize pygame, settings and screen object"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pirate attack")

    # Create an instance to store the game stats
    stats = GameStats(ai_settings)

    # Make a ship, a group of aliens and a group of bullets
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Create an alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the mainloop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
