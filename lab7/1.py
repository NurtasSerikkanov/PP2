import pygame
from datetime import datetime
pygame.init()

#global Variables
WIDTH=800
HEIGHT=600
FPS=20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PLUM = (221, 160, 221)
YELLOW = (255, 255, 0)
BLUE2 = (0, 255, 255)

def blitRotateCenter(surf, image, topleft, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

#Initializing
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TEST PROGRAM')

#img
mickey=pygame.image.load('./img/mickey.jpeg')
mickey=pygame.transform.scale(mickey, (WIDTH, HEIGHT))
a2=pygame.image.load('./img/ruka2.png')
a1=pygame.image.load('./img/ruka1.png')

# font=pygame.font.Font('./font/bebas.ttf')

clock=pygame.time.Clock()

finished=False

def time(time):
    return 360-time*6

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finished=True

    screen.blit(mickey, (0, 0))
    # screen.blit(a1, (WIDTH//2-148, HEIGHT//2-120))
    # screen.blit(a2, (WIDTH//2, HEIGHT//2-131))

    t=datetime.now()

    angle_sec=time(t.second+1)
    angle_min=time(t.minute)

    blitRotateCenter(screen, a1, (180, 90), angle_sec)
    blitRotateCenter(screen, a2, (180, 90), angle_min)

    pygame.display.flip()
pygame.quit()