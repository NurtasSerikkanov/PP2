from random import randint, randrange
import psycopg2
import csv
import pygame
username = input()
config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port=5432,
    user='postgres',
    password='t$hZw!Kz'
)

current = config.cursor()

sql = '''
    SELECT * FROM user_snake WHERE user_name = %s;
'''
current.execute(sql, [username])
data = current.fetchone()

# print(type(data))

try:
    score = data[1]
    highscore = data[2]
    level = data[3]
except:
    score = 0
    highscore = 0
    level = 0

if data == None:
    sql = '''
        INSERT INTO user_snake VALUES(%s, 0, 0, 0);
    '''
    current.execute(sql, [username])
    config.commit()
pygame.init()

WIDTH, HEIGHT = 800, 640
FPS = 5
cell = 40

font = pygame.font.SysFont("Proxima Nova", 40, True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221, 160, 221)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

finished = False

clock = pygame.time.Clock()


class Food:
    def __init__(self):
        # self.x = randint(0, WIDTH) % cell * 40
        # self.y = randint(0, HEIGHT) % cell * 40
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
        if level == 1:
            self.x = randrange(cell, WIDTH - cell, cell)
            self.y = randrange(0, HEIGHT, cell)
        if level > 1:
            self.x = randrange(cell, WIDTH - cell, cell)
            self.y = randrange(cell, HEIGHT - cell, cell)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell))

    def redraw(self):
        self.x = randrange(cell, WIDTH - cell, cell)
        self.y = randrange(cell, HEIGHT - cell, cell)


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell))


class Snake:
    def __init__(self):
        self.speed = cell
        self.score = 0
        self.body = [[80, 80], [1000, 1000], [
            1040, 1040], [1080, 1080], [1120, 1120]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN

    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_d and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_w and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_s and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color,
                             (block[0], block[1], cell, cell))

    def collide_food(self, f: Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            f.redraw()
            self.score += 1
            self.body.append([1000, 1000])

    def collide_self(self):
        global finished
        if self.body[0] in self.body[1:]:
            finished = True

    def check_food(self, f: Food):
        if [f.x, f.y] in self.body:
            f.redraw()

# try:
#     sql1 = 

s = Snake()
f = Food()


while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        #     level += 1
        #     level %= 2

    screen.fill(WHITE)
    if s.score in range(5, 10):
        level = 1
        FPS = 6

    if s.score in range(10, 15):
        level = 2
        FPS = 7
    if s.score in range(15, 20):
        level = 3
        FPS = 9
    if s.score in range(20,25):
        level = 4
        FPS = 11
    if score in range(25, 30):
        level = 5
        FPS = 13
    if score >= 30:
        level = 6
        FPS = 17

    for i in range(0, WIDTH, cell):
        for j in range(0, HEIGHT, cell):
            pygame.draw.rect(screen, BLACK, (i, j, cell, cell), 1)

    walls_coor = open(f'wall{level}.txt', 'r').readlines()

    walls = []

    for i, line in enumerate(walls_coor):
        for j, each in enumerate(line):
            if each == "#":
                walls.append(Wall(j * cell, i * cell))
    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y:
            f.redraw()

        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
            finished = True
    if score > highscore:
        highscore = score
        sql = '''
        UPDATE user_snake SET score = %s, highscore = %s, level = %s WHERE user_name = %s;
        '''
        current.execute(sql, [score, highscore, level, username])
        
    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)

    text = font.render(f"Score:{s.score}", True, BLACK)
    text2 = font.render(f"Level: {level}", True, BLACK)
    text3 = font.render(f"Highscore: {highscore}", True, BLACK)
    screen.blit(text, (0, 0))
    screen.blit(text2, (0, 40))
    screen.blit(text3,(0,80))
    pygame.display.flip()
    score = s.score
pygame.quit()
if score > highscore:
    highscore = score
    score = 0
    level = 0
    sql = '''
        UPDATE user_snake SET score = %s, highscore = %s, level = %s WHERE user_name = %s;
    '''
    current.execute(sql, [score, highscore, level, username])
else:
    score = 0
    level = 0
    sql = '''
        UPDATE user_snake SET score = %s, level = %s WHERE user_name = %s;
    '''
    current.execute(sql,[score, level, username])
sql = '''
    SELECT * FROM user_snake;
'''
current.execute(sql, [username])
data = current.fetchall()
print(*data, sep = ",")

f = open("SCORE TABLE.csv", 'w')
writer = csv.writer(f)

writer.writerow(data)
f.close()


config.commit()
current.close()
config.close()