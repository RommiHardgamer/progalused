import pygame.font

class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)

        self.prepare_score()
        self.prepare_level()
        self.prepare_high_score()

    def prepare_score(self):
        score_str = str(self.stats.score) 
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prepare_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.game_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_image_rect.right
        self.level_rect.top = self.score_image_rect.bottom + 10

    def prepare_high_score(self):
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def draw_score(self):
        self.prepare_score()
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
