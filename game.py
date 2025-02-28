import pygame
from setting import Settings
from player import Player
import game_functions as gf
from bubble import Bubble
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    gm_settings = Settings()
    
    screen = pygame.display.set_mode((gm_settings.screen_width, gm_settings.screen_height))
    pygame.display.set_caption(gm_settings.caption)
    
    play_button = Button (gm_settings, screen, "Play")
    
    status = GameStats()
    
    sb = Scoreboard(gm_settings, screen,stats)

    clock = pygame.time.Clock()
   
    player = Player(screen)
    
    bubbles = pygame.sprite.Group()

    
    while True:
        gf.check_events(gm_settings, screen, player, bubble)
        if stats.game_active:
            gf.update_bubbles(player, bubbles, stats, sb, gm_settings)
            player.update()
            bubble.update()
        else:
            bubble.empty()
        gf.update_screen(gm_settings, screen, player, bubble, clock,stats,play_button)

run_game()