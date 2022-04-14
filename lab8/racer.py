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
        self.image=pygame.transform.scale(pygame.image.load('./img/Gold_1.png'), (25, 25))
        self.surf=pygame.Surface((25, 25), pygame.SRCALPHA)
        self.rect=self.surf.get_rect(center=(self.x, self.y))
    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, self.rect)
    def move(self):
        self.rect.move_ip(0, self.speed)
    def kil(self):
        if self.rect.top>HEIGHT:
            self.kill()

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

        for coin in coins:
            if pygame.sprite.collide_rect(p, coin):       # егер Player мен Coin кактыгысып калса SCORE кобейеди ягни акша саны
                coin.kill()
                SCORE+=1
                coins.add(Coin())
        
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