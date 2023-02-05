import pygame.font
from pygame.sprite import Sprite

class HelpInfo(Sprite):
    """Класс для вывода помощи"""

    def __init__(self, ai_game):
        """Инициализирует пмощь и её начальную позицию"""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Загружает изображение помощи и получает прямоугольник.
        self.image = pygame.image.load('images/helps.bmp')
        self.rect = self.image.get_rect()
        
        # Подсказака появляется у нижнего края.
        self.rect.topleft = (445, 550)

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)