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

    def prep_scrore(self):
        """Преобразует текущий счёт в графическое изображение."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
                self.text_color, self.settings.bg_color)

        # Вывод счёта в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20