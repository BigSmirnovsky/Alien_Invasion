class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 900 
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamyc_settings()

    def initialize_dynamyc_settings(self):
        """Инициализирует настройки, динамические настройки игры"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        