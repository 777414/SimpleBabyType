import pygame
import utils

pygame.init()
pygame.display.set_caption("Simple BabyType")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# окно
WIDTH = 400
HEIGHT = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont("Times New Roman", 60)

clock = pygame.time.Clock()
lvl = utils.create_lvl(100)
miss = False
last_time = pygame.time.get_ticks()
time_left = 3.0
timer_work = True
FPS = 60
running = True
while running:
    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000.0
    last_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if len(lvl) == 0 or not timer_work:
                continue

            pk = event.unicode.lower()
            if pk.isalpha():
                if pk == lvl[0]:
                    lvl.pop(0)
                    miss = False
                    time_left += 2.0
                else:
                    miss = True
                    time_left -= 5.0
    
    if timer_work:
        time_left -= delta_time
        if time_left <= 0:
            time_left = 0
            timer_work = False
    
    if len(lvl) == 0:
        timer_work = False

    screen.fill(WHITE)
    x, y = 0, 0
    for i, letter in enumerate(lvl):
        text = font.render(letter.upper(), True, WHITE)
        clr = RED if (i == 0 and miss) else BLUE
        pygame.draw.rect(screen, clr, (x,y, 50,60))
        text_rect = text.get_rect(center=(x + 25, y + 30))
        screen.blit(text, text_rect)
        x += 60
    
    timer_text = font.render(f"{time_left:.1f}", True, BLUE)
    timer_rect = timer_text.get_rect(centerx=WIDTH // 2, y = 100)
    screen.blit(timer_text, timer_rect)
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()