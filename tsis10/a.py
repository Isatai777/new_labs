import pygame
import random
import math

pygame.init()

W, H = 700, 500
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

win = pygame.display.set_mode((W, H))
pygame.display.set_caption("STPD GAME HAHA!")
pygame.display.set_icon(pygame.image.load("C:/Users/OMATA/Desktop/pp2/tsis9/pop.png"))

RECT_W = 60
RECT_H = 40
rect = pygame.Rect(W // 2, H // 2, RECT_W, RECT_H)
rect_img = pygame.image.load('C:/Users/OMATA/Desktop/pp2/tsis9/pop.png')
rect_img = pygame.transform.scale(rect_img, (RECT_W, RECT_H))

circles = [(random.randint(50, W - 50), random.randint(50, H - 50), random.randint(3, 7)) for _ in range(5)]
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(5)]

counters = {"LEFT": 0, "RIGHT": 0, "UP": 0, "DOWN": 0, "CIRCLES": 0}

victory_audio = pygame.mixer.Sound("violin-win-5-185128.mp3")

FPS = 140
speed = 5

speed_bonus_rect = None
size_bonus_rect = None
bonus_timer = 0
speed_bonus_active_timer = 0
size_bonus_active_timer = 0
speed_bonus_active = False
size_bonus_active = False

running = True

def distance(rect, circle):
    dx = rect.centerx - circle[0]
    dy = rect.centery - circle[1]
    return math.sqrt(dx ** 2 + dy ** 2)

def move():
    for i, circle in enumerate(circles):
        if distance(rect, circle) < 50:
            dx, dy = (circle[0] - rect.centerx), (circle[1] - rect.centery)
            dx, dy = dx / 2, dy / 2
            new_x = min(max(circle[0] + dx, 50), W - 50)
            new_y = min(max(circle[1] + dy, 50), H - 50)
            circles[i] = (new_x, new_y, circle[2])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and rect.left > 0:
                rect.move_ip(-speed, 0)
                counters["LEFT"] += 1
            elif event.key == pygame.K_RIGHT and rect.right < W:
                rect.move_ip(speed, 0)
                counters["RIGHT"] += 1
            elif event.key == pygame.K_UP and rect.top > 0:
                rect.move_ip(0, -speed)
                counters["UP"] += 1
            elif event.key == pygame.K_DOWN and rect.bottom < H:
                rect.move_ip(0, speed)
                counters["DOWN"] += 1

    move()

    circlesToRemove = []

    for i, circle in enumerate(circles):
        if rect.collidepoint(circle[0], circle[1]):
            counters["CIRCLES"] += 1
            circlesToRemove.append(i)

    for i in sorted(circlesToRemove, reverse=True):
        del circles[i]
        del colors[i]
    
    if len(circles) == 0:
        circles = [(random.randint(50, W - 50), random.randint(50, H - 50), random.randint(3, 7)) for _ in range(5)]
        colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(5)]
        victory_audio.play()
    
    bonus_timer += 1
    if bonus_timer > FPS * 10:
        speed_bonus_rect = pygame.Rect(random.randint(0, W - 20), random.randint(0, H - 20), 20, 20)
        size_bonus_rect = pygame.Rect(random.randint(0, W - 20), random.randint(0, H - 20), 20, 20)
        bonus_timer = 0
    

    if speed_bonus_rect and rect.colliderect(speed_bonus_rect):
        speed *= 2
        speed_bonus_active = True
        speed_bonus_active_timer = FPS * 7
        speed_bonus_rect = None
    

    if size_bonus_rect and rect.colliderect(size_bonus_rect):
        rect.width *= 2
        rect.height *= 2
        rect_img = pygame.transform.scale(rect_img, (rect.width, rect.height))
        size_bonus_active = True
        size_bonus_active_timer = FPS * 7
        size_bonus_rect = None
    

    if speed_bonus_active:
        speed_bonus_active_timer -= 1
        if speed_bonus_active_timer <= 0:
            speed /= 2
            speed_bonus_active = False
    
    if size_bonus_active:
        size_bonus_active_timer -= 1
        if size_bonus_active_timer <= 0:
            rect.width //= 2
            rect.height //= 2
            rect_img = pygame.transform.scale(rect_img, (rect.width, rect.height))
            size_bonus_active = False
    
    win.fill(WHITE)
    pygame.draw.rect(win, BLUE, rect)

    for i, circle in enumerate(circles):
        pygame.draw.circle(win, colors[i], (int(circle[0]), int(circle[1])), circle[2])
    win.blit(rect_img, rect)
    
    if speed_bonus_rect:
        pygame.draw.rect(win, GREEN, speed_bonus_rect)
    
    if size_bonus_rect:
        pygame.draw.rect(win, RED, size_bonus_rect)
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"LEFT: {counters['LEFT']}, RIGHT: {counters['RIGHT']}, UP: {counters['UP']}, DOWN: {counters['DOWN']}, CIRCLES: {counters['CIRCLES']}", 1, (10, 10, 10))
    win.blit(text, (20, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()












