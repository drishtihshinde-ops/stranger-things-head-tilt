import pygame
pygame.mixer.init()
sound = pygame.mixer.Sound("assets/vecna_clock.wav")
sound.play()
input("Press Enter to stop...")
