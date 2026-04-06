import pygame
import utils

pygame.init()
pygame.display.set_caption("Simple BabyType")

# окно
WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont("Times New Roman", 60)

clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    text = font.render("A", True, WHITE)
    pygame.draw.rect(screen, BLUE, (180,180, 50,60))
    text_rect = text.get_rect(center=(180 + 25, 180 + 30))
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()