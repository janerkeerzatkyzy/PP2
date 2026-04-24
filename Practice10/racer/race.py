import pygame, sys
from pygame.locals import *
import random, time
pygame.init()
pygame.mixer.init()
FPS = 60
Frame = pygame.time.Clock()
black = (0, 0, 0)
red   = (255, 0, 0)

WIDTH = 400
HEIGHT = 600

speed = 5
score = 0
coins_num = 0

font = pygame.font.SysFont("Arial", 60)
font_small = pygame.font.SysFont("Arial", 20)
game_over = font.render("GAME OVER", True, black)
background = pygame.image.load("material/AnimatedStreet.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

try:
    pygame.mixer.music.load("material/1song.mp3")
    pygame.mixer.music.play(-1)
except:
    print("Error")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("material/Player.png").convert_alpha()
        self.rect = self.image.get_rect(center = (160, 520))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("material/Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.respawn()

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            score += 1
            self.respawn()

    def respawn(self):
        self.rect.center = (
            random.randint(40, WIDTH - 40),
            random.randint(-300, -100)
        )

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("material/coin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.respawn()

    def move(self):
        self.rect.move_ip(0, max(2, speed - 3))
        if self.rect.top > HEIGHT:
            self.respawn()

    def respawn(self):
        while True:
            x = random.randint(40, WIDTH - 40)
            y = random.randint(-600, -100)

            if abs(x - P1.rect.centerx) > 80:
                self.rect.center = (x, y)
                break

P1 = Player()
E1 = Enemy()

coins = pygame.sprite.Group()
for _ in range(3):
    coins.add(Coin())

enemies = pygame.sprite.Group(E1)

all_sprites = pygame.sprite.Group(P1, E1, *coins)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.2

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    score_text = font_small.render(f"SCORE: {score}", True, black)
    screen.blit(score_text, (10, 10))

    coin_text = font_small.render(f"COINS: {coins_num}", True, black)
    screen.blit(coin_text, (WIDTH - 130, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    collected = pygame.sprite.spritecollide(P1, coins, True, pygame.sprite.collide_mask)

    for _ in collected:
        coins_num += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    if pygame.sprite.spritecollideany(P1, enemies, pygame.sprite.collide_mask):
        pygame.mixer.music.pause()
        try:
            pygame.mixer.Sound("material/crash.wav").play()
        except:
            pass
        time.sleep(0.1)
        screen.fill(red)
        screen.blit(game_over, (45, 250))
        pygame.display.update()
        time.sleep(3)

        pygame.quit()
        sys.exit()
    pygame.display.update()
    Frame.tick(FPS)