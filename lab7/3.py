import pygame
pygame.init()

WIDTH, HEIGHT=800, 600
FPS=40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PLUM = (221, 160, 221)
YELLOW = (255, 255, 0)
BLUE2 = (0, 255, 255)

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TEST')

clock=pygame.time.Clock()

finished=False

c_x, c_y = WIDTH//2, HEIGHT//2
RAD=25
step=15

while not finished:
    clock.tick(FPS)

    screen.fill(WHITE)

    keydown=pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finished=True
        # if event.type==pygame.KEYDOWN:
        #     if event.key==pygame.K_RIGHT and c_x+RAD<WIDTH:
        #         c_x+=step
        #     if event.key==pygame.K_LEFT and c_x-RAD>0:
        #         c_x-=step
        #     if event.key==pygame.K_UP and c_y-RAD>0:
        #         c_y-=step
        #     if event.key==pygame.K_DOWN and c_y+RAD<HEIGHT:
        #         c_y+=step
        
    if keydown[pygame.K_RIGHT] and c_x+RAD<WIDTH:
        c_x+=step
    if keydown[pygame.K_LEFT] and c_x-RAD>0:
        c_x-=step
    if keydown[pygame.K_UP] and c_y-RAD>0:
        c_y-=step
    if keydown[pygame.K_DOWN] and c_y+RAD<HEIGHT:
        c_y+=step
    
    pygame.draw.circle(screen, RED, (c_x, c_y), RAD)

    pygame.display.flip()
pygame.quit()