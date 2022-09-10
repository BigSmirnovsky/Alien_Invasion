import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Классб представляющий одного пришельца"""
    
    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen

        #Закргузка изображения и назначение атрибута rect
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизотальной позиции пришельца
        self.x = float(self.rect.x)