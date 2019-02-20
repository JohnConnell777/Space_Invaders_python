import pygame


class Beam(pygame.sprite.Sprite):

    def __init__(self, ai_settings, screen, alien):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('resources/Images/alienblast.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.beam_speed_factor

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
