import sys
import pygame
from settings import Settings


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("game test")
    bg_color = ai_setting.bg_color
    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()
