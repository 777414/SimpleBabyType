import pygame
import utils

pygame.init()
pygame.display.set_caption("Simple BabyType")

# окно
WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Times New Roman", 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    txt = font.render("Hello!", True, (255,255,255))
    screen.blit(txt, (100,100))

    pygame.display.update()

pygame.quit()