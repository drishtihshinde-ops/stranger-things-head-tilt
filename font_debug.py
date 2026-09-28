import pygame
pygame.init()

try:
    font = pygame.font.Font("assets/st_font.ttf", 40)
    print("FONT LOADED SUCCESSFULLY")
except Exception as e:
    print("FONT ERROR:", e)
