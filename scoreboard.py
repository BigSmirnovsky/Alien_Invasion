import pygame.font

class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai_game):
        """Инициализирует атрибуты посдчета очков"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки шрифта для вывода счёта.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка изображения счетов.
        self.prep_score()
        self.prep_hight_score()
        self.prep_level()

    def prep_score(self):
        """Преобразует текущий счёт в графическое изображение."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, 
                self.text_color, self.settings.bg_color)

        # Вывод счёта в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счёт на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)

    def prep_hight_score(self):
        """Преобразует рекорднаый счёт в графическое изображение"""
        hight_score = round(self.stats.hight_score, -1)
        hight_score_str = "{:,}".format(hight_score)
        self.hight_score_image = self.font.render(hight_score_str, True,
                self.text_color, self.settings.bg_color)

        # Рекорд выравнивается по центру верхней стороны.
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.score_rect.top

    def check_hight_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.hight_score:
            self.stats.hight_score = self.stats.score
            self.prep_hight_score()
    
    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)

        # Уровень выводится под текущим счётом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
