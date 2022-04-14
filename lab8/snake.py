import pygame
from random import randint, randrange
pygame.init()

WIDTH, HEIGHT=600, 600
FPS=5
cell=30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)
YELLOW=(255, 255, 0)
BLUE2 = (0, 255, 255)
ORANGE=(255, 165, 0)

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SNAKE')

clock=pygame.time.Clock()

font=pygame.font.SysFont('Times New Roman', 100 , False, False)
font1=pygame.font.SysFont('Times New Roman', 20 , False, False)

class Food:
    def __init__(self):
        self.x=randrange(0, WIDTH, cell)            # кез келген жерден пайда болады
        self.y=randrange(0, HEIGHT, cell)
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell))
    def redraw(self):
        self.x=randrange(0, WIDTH, cell)      
        self.y=randrange(0, HEIGHT, cell)

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def draw(self):
        pygame.draw.rect(screen, PURPLE, (self.x, self.y, cell, cell))

class Snake:
    def __init__(self):
        self.speed=cell
        self.body=[[60, 60]]     # жылан басынын координатасы
        self.dx=0   
        self.dy=self.speed          # жыланнын алгашкы козгалысы
        self.destination=''
        self.color=GREEN

    def move(self, events):
        for event in events:
            if event.type==pygame.KEYDOWN: 
                if event.key==pygame.K_a and self.destination!='right':    #егер жылан солға бағытталса онда ол 180 градуска ягни онга бурыоа алмайды
                    self.dx=-self.speed
                    self.dy=0
                    self.destination='left'
                if event.key==pygame.K_d and self.destination!='left':  # егер жылан онга багытталса солга бурыла алмайды
                    self.dx=self.speed
                    self.dy=0
                    self.destination='right'
                if event.key==pygame.K_w and self.destination!='down':  # егер жылан жогары багытталса томенге бурыла алмацды
                    self.dx=0
                    self.dy=-self.speed
                    self.destination='up'
                if event.key==pygame.K_s and self.destination!='up':    # егер жылан томен багытталса жогарыга бурыла алмайды
                    self.dx=0
                    self.dy=self.speed
                    self.destination='down'

        for i in range(len(self.body)-1, 0, -1):    # сонгы координаталыра бастапкы координатасынын изимен журеди
            self.body[i][0]=self.body[i-1][0]
            self.body[i][1]=self.body[i-1][1]
        
        self.body[0][0]+=self.dx
        self.body[0][1]+=self.dy

        self.body[0][0]%=WIDTH
        self.body[0][1]%=HEIGHT

    def draw(self):
        for block in self.body:     # жыланнын басынан кейинги денесин шыгарады
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))

    def collide_food(self, f:Food):
        global SCORE
        if self.body[0][0]==f.x and self.body[0][1]==f.y:   # жылан тамакпен кездессе жыланнын денеси артады
            self.body.append([1000, 1000]) 
            SCORE+=1 
    
    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:     # жылан тамакпен кездессе, тамак баска координата кайтадан салынады
            f.redraw()

    def collide_self(self):
        global lose
        if self.body[0] in self.body[1:]:   # жылан оз денесимен согылса ойын аякталады
            lose=True

finished=False
restart=True
win=False
lose=False

while restart:
    f=Food()
    s=Snake()

    SCORE=0
    level=0

    finished=False
    win=False
    lose=False

    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        events=pygame.event.get()

        for event in events:
            if event.type==pygame.QUIT:
                finished=True
                restart=False
            # if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
            #     level+=1
            #     level%=4

        walls_coor=open('wall0.txt', 'r').readlines()     # стенаны шыгарады

        if SCORE in range(3, 7):
            walls_coor=open('wall1.txt', 'r').readlines()   # стена озгереди
        if SCORE in range(7, 10):
            walls_coor=open('wall2.txt', 'r').readlines()
        if SCORE>=10:
            walls_coor=open('wall3.txt', 'r').readlines()
                
        # walls_coor=open(f'wall{level}.txt', 'r').readlines()

        walls=[]

        for i, line in enumerate(walls_coor):
            for j, each in enumerate(line):
                if each == '#':
                    walls.append(Wall(j*cell, i*cell))      # баска файлды оку аркылы стеналар жасайды

        

        f.draw()
        s.draw()
        s.move(events)
        s.collide_food(f)
        s.check_food(f)
        s.collide_self()

        for wall in walls:
            wall.draw()
            if f.x == wall.x and f.y == wall.y:         # тамак стенадан шыкпайды
                f.redraw
            if s.body[0][0]==wall.x and s.body[0][1]==wall.y:   # жылан стенага согылса ойын аякталады
                lose=True

        for i in range(0, WIDTH, cell):
            for j in range(0, HEIGHT, cell):
                pygame.draw.rect(screen, ORANGE, (i, j, cell, cell), 1)   

        score=font1.render(f'SCORE: {SCORE}', True, YELLOW)
        screen.blit(score, (10, 560))

        while lose or win:
            pygame.draw.rect(screen, RED, (WIDTH//2-250, HEIGHT//2-250, 500, 500))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    finished=True
                    restart=False
                    lose=False
                    win=False
                if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
                    finished=True
                    lose=False
                    win=False
             
            game_over=font.render('GAME OVER', True, YELLOW)
            if lose:
                pos=game_over.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.blit(game_over, pos)

            pygame.display.flip()
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()