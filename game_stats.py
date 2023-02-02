import json
class GameStats():
    """Отслеживает статистику для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
         
        with open('record.json') as f:
            self.stats = json.load(f)
                 
        # Рекорд не должен сбрасываться.
        self.hight_score = self.stats["record_score"]
        
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходу игры."""
        with open('record.json') as f:
            self.stats = json.load(f)
        
        self.ship_left = self.settings.ship_limit
        self.score = self.stats["score"]
        self.level = self.stats["level"]
           
    # def save_record_stat(self, record_stat):
    #     """Сохранение файла рекарда"""
    #     with open('record.json', 'w') as f:
    #         f.write(json.dumps(record_stat))
