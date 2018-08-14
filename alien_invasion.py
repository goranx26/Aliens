import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    """Initialize pygame, settings and screen object"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pirate attack")

    # Make a ship, a group of aliens and a group of bullets
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Create an alien fleet
    gf.create_fleet(ai_settings, screen, aliens)

    # Start the mainloop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
