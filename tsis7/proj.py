import pygame
import pygame.display

pygame.init()

W,H = 600,400
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

win = pygame.display.set_mode(( W, H))
pygame.display.set_caption("STPD GAME HAHA!")
pygame.display.set_icon(pygame.image.load("C:/Users/OMATA/Desktop/pp2/tsis7/pop.png"))


RECT_W = 60
RECT_H = 40
rect = pygame.Rect(W // 2, H // 2, RECT_W, RECT_H)

counters = {"LEFT": 0, "RIGHT": 0, "UP": 0, "DOWN": 0}

FPS = 140

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-5, 0)
                counters["LEFT"] += 1
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(5, 0)
                counters["RIGHT"] += 1
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -5)
                counters["UP"] += 1
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 5)
                counters["DOWN"] += 1
    
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0 , 255), rect)
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"LEFT: {counters['LEFT']}, RIGHT: {counters['RIGHT']}, UP: {counters['UP']}, DOWN: {counters['DOWN']}", 1, (10, 10, 10))
    win.blit(text, (20, 20))

    pygame.display.flip()
   
pygame.quit()