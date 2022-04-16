from tracemalloc import start
import pygame
from math import sin, cos, pi
pygame.init()

WIDTH, HEIGHT=800, 600
FPS=60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)
YELLOW=(255, 255, 0)
BLUE2 = (0, 255, 255)

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PAINT')

clock=pygame.time.Clock()

img=pygame.transform.scale(pygame.image.load('./img/paint.jpg'), (150, 150))  #цветтардын фотосын қою

def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)  

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos):
    pygame.draw.circle(screen, WHITE, pos, RAD)

def drawSqu(color, pos, width):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, width), 4)

def drawtriangle(color, pos):
    pygame.draw.polygon(screen, color, pos, 3)

def drawRight_triangle(color, pos, x3, y3):
    pygame.draw.polygon(screen, color, [pos, (x3, y3)],  3)

def drawRRhom(color, pos, width):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, width), 4)

finished=False

screen.fill(pygame.Color('white'))

drawing=False
color=pygame.Color('black')

start_pos=0
end_pos=0

RAD=30

mode=0
# 0-rectangle
# 1-circle
# 2-eraser

while not finished:
    clock.tick(FPS)

    pos=pygame.mouse.get_pos()
    screen.blit(img, (10, 10))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finished=True

        if event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True
            start_pos=pos
            if pos[0]>10 and pos[0]<160 and pos[1]>10 and pos[1]<160:
                color=screen.get_at(pos)

        if event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            end_pos=pos
            rect_x=abs(start_pos[0]-end_pos[0])         # центр прямоугольника
            rect_y=abs(start_pos[1]-end_pos[1])
            circ_x=abs(start_pos[0]+rect_x//2)          # центр круга
            circ_y=abs(start_pos[1]+rect_y//2)
            tri_x=abs(start_pos[0]-end_pos[0])
            x3 = (end_pos[0] - start_pos[0]) * cos(pi/3) - (end_pos[1] - start_pos[1]) * sin(pi/3) + start_pos[0]
            y3 = (end_pos[0] - start_pos[0]) * sin(pi/3) + (end_pos[1] - start_pos[1]) * cos(pi/3) + start_pos[1]
            if mode==0:
                drawRect(color, start_pos, rect_x, rect_y)
            if mode==1:
                drawCircle(color, (circ_x, circ_y), rect_x//2)
            if mode==3:
                drawSqu(color, start_pos, rect_x)
            if mode==4:
                drawtriangle(color, [start_pos, end_pos, (start_pos[0], end_pos[1])])
            if mode==5:
                drawtriangle(color, [start_pos, end_pos, (x3, y3)])

        if event.type==pygame.MOUSEMOTION and drawing:
            if mode==2:
                eraser(pos)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                mode+=1
                mode%=6
            if event.key==pygame.K_z:
                RAD+=3 and RAD<WIDTH//2       # радиус eraser увеличивается
            if event.key==pygame.K_x:
                RAD-=3 and RAD>0                # радиус eraser уменьшается
            if event.key==pygame.K_BACKSPACE:
                screen.fill(pygame.Color('white'))    # очищаеть все что было в скрине

        

    pygame.display.flip()
pygame.quit()