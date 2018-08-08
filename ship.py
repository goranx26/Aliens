import pygame

class Ship():

    def __init__(self, screen):
        """initialize the ship and set starting position"""
        self.screen = screen

        # Load ship image and get its rect
        self.image = pygame.image.load('images/gube.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
