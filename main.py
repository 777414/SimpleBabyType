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
lvl = utils.create_lvl(100)
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    x, y = 0, 0
    for i, letter in enumerate(lvl):
        text = font.render(letter.upper(), True, WHITE)
        pygame.draw.rect(screen, BLUE, (x,y, 50,60))
        text_rect = text.get_rect(center=(x + 25, y + 30))
        screen.blit(text, text_rect)
        x += 60
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()