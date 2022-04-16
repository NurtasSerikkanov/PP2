import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT=800, 600
FPS=20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)
YELLOW=(255, 255, 0)
BLUE2 = (0, 255, 255)

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RACER')

background=pygame.transform.scale(pygame.image.load('./img/bg.jpeg'), (WIDTH, HEIGHT))
bgY=0
bgY2=-background.get_height()
BGSPEED=7

font=pygame.font.SysFont('Times New Roman', 20, False, False)
font1=pygame.font.SysFont('Times New Roman', 80, False, False)

clock=pygame.time.Clock()

MEGA_COIN=pygame.USEREVENT+1
FREEZE=pygame.USEREVENT+2
FLIP=pygame.USEREVENT+3

pygame.time.set_timer(FLIP, 150)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x=400
        self.y=500
        self.speed=15
        self.image=pygame.transform.scale(pygame.image.load('./img/Audi.png'), (40, 90))
        self.surf=pygame.Surface((40, 90), pygame.SRCALPHA)        # SRCALPHA-фотонын фонын алып тастайды
        self.rect=self.surf.get_rect(center=(self.x, self.y))
    def draw(self):
        self.surf.blit(self.image, (0, 0))           # фото коямын
        screen.blit(self.surf, self.rect)
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left>=85:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right<=WIDTH-85:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_UP] and self.rect.top>=0:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_DOWN] and self.rect.bottom<=HEIGHT:
            self.rect.move_ip(0, self.speed)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x=randint(85, WIDTH-85)
        self.y=-100
        self.speed=randint(10, 15)
        self.image=pygame.transform.scale(pygame.image.load('./img/Police.png'), (40, 90))
        self.surf=pygame.Surface((40, 90), pygame.SRCALPHA)
        self.rect=self.surf.get_rect(center=(self.x, self.y))
    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, self.rect)
    def move(self):
        self.rect.move_ip(0, self.speed)
    def kil(self):
        if self.rect.top>HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x=randint(85, WIDTH-85)
        self.y=-100
        self.speed=randint(10, 15)
        self.random_number = randint(0, 9)
        self.animation_index = 0
        self.images=[
            './img/Coin/c1.png',
            './img/Coin/c2.png',
            './img/Coin/c3.png',
            './img/Coin/c4.png',
            './img/Coin/c5.png',
            './img/Coin/c6.png'
        ]
        self.image=pygame.transform.scale(pygame.image.load(self.images[0]), (20, 20))
        self.surf=pygame.Surface((25, 25), pygame.SRCALPHA)
        self.rect=self.surf.get_rect(center=(self.x, self.y))
        self.mega_coin()
    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, self.rect)
    def move(self):
        self.rect.move_ip(0, self.speed)
    def kil(self):
        if self.rect.top>HEIGHT:
            self.kill()

    def animate(self):
        self.animation_index += 1
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.image = pygame.image.load(self.images[self.animation_index])

    def mega_coin(self):
        if self.random_number in [0, 1, 2]:
            self.image = pygame.image.load(self.images[1])
            # self.speed = 15
        else:
            self.image = pygame.image.load(self.images[0])

    def is_mega_coin(self):
        return self.random_number == 5

restart=True
finished=False
lose=False

while restart:     # играть занова
    finished=False
    lose=False

    SCORE=0

    p=Player()
    enemies=pygame.sprite.Group([Enemy() for i in range(5)])
    coins=pygame.sprite.Group([Coin() for i in range(7)])

    while not finished:
        clock.tick(FPS)
        screen.blit(background, (0, bgY))
        screen.blit(background, (0, bgY2))

        if bgY>background.get_height():                # сурет битип жатканда усти жагынан кайтадан пайда болып жатады
            bgY=-background.get_height()
        if bgY2>background.get_height():                # скринда бос орын калып калмас ушин еки сурет орнатылган
            bgY2=-background.get_height()

        bgY+=BGSPEED                        # главный сурет козгалады
        bgY2+=BGSPEED

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                finished=True
                restart=False
            if event.type == MEGA_COIN:
                p.speed = 30
            if event.type == FLIP:
                for coin in coins:
                    coin.animate()

        p.draw()
        p.move()

        if len(enemies)<5:               # егер enemy 5 тен аз боып кетсе, олардын саны 5 болганга дейин тагы enemy саны косылады
            enemies.add(Enemy())
        if len(coins)<5:
            coins.add(Coin())

        for coin in coins:
            coin.draw()
            coin.move()
            coin.kil()

        for enemy in enemies:
            enemy.draw()
            enemy.move()
            enemy.kil()

        if pygame.sprite.spritecollide(p, enemies, False):      # егер Player мен Enemy кактыгысып калса ойын аякталады
            lose=True

        for coin in pygame.sprite.spritecollide(p, coins, True):
            SCORE += 1
            if coin.is_mega_coin():
                SCORE += 100
                pygame.time.set_timer(MEGA_COIN, 5000, loops=False)
        
        for enemy in enemies:
            for enemy2 in enemies:
                if enemy!=enemy2 and pygame.sprite.collide_rect(enemy, enemy2):   # егер еки enemy бир жерден шыкса олардын скринда тек биреуи гана пайда болады
                    enemy2.kill()
        
        for coin in coins:
            for coin2 in coins:
                if coin!=coin2 and pygame.sprite.collide_rect(coin, coin2):    # егер еки coin бир жерден шыкса олардын скринда тек биреуи гана пайда болады
                    coin2.kill()
        
        score=font.render(f'SCORE: {SCORE}', True, RED)
        screen.blit(score, (10, 10))

        while lose:
            pygame.draw.rect(screen, RED, (WIDTH//2-250, HEIGHT//2-200, 500, 400))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    finished=True
                    lose=False
                    restart=False
                if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
                    finished=True
                    lose=False
            if lose:
                game_over=font1.render('GAME_OVER', True, YELLOW)
                pos=game_over.get_rect(center=(WIDTH//2, HEIGHT//2))
                screen.blit(game_over, pos)
                    
            pygame.display.flip()
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()