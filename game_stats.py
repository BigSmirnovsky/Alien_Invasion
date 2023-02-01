import json
class GameStats():
    """Отслеживает статистику для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
              
        # Рекорд не должен сбрасываться.
        self.hight_score = self.load_record_stat()
        
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходу игры."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
    def load_record_stat(self):
        """Загрузка статы"""    
        with open('record.json') as f:
            self.stats = json.load(f)
        return self.stats["stat"]
    
    def save_record_stat(self, record_stat):
        """Сохранение файла рекарда"""
        with open('record.json', 'w') as f:
            f.write(json.dumps(record_stat))
