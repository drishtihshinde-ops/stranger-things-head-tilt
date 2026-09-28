import pygame
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Which Stranger Things Character Are You?")

clock = pygame.time.Clock()

# Colors
BLACK = (10, 10, 10)
RED = (180, 0, 0)
WHITE = (230, 230, 230)

# Fonts (your font path is CORRECT)
title_font = pygame.font.Font("assets/st_font.ttf", 50)
text_font = pygame.font.Font("assets/st_font.ttf", 26)

# Question data
question = "Adventure or Mystery?"
left_option = "Adventure"
right_option = "Mystery"

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Title
    title = title_font.render("STRANGER THINGS", True, RED)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))

    # Question
    q_text = text_font.render(question, True, WHITE)
    screen.blit(q_text, (WIDTH//2 - q_text.get_width()//2, 180))

    # Options
    left_text = text_font.render("LEFT  ←  " + left_option, True, RED)
    right_text = text_font.render("RIGHT  →  " + right_option, True, RED)

    screen.blit(left_text, (150, 300))
    screen.blit(right_text, (WIDTH - 350, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
