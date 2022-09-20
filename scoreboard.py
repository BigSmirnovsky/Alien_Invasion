import pygame.font

class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai_game):
        """Инициализирует атрибуты посдчета очков"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.stats

        # Настройки шрифта для вывода счёта.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # подготовка исходного изображения.
        self.prep_score()