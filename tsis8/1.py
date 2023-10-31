import pygame
import sys
from pygame.locals import *
import random, time

pygame.init()

fps = 60
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width_, height = 400, 600
speed = 5
score = 0
coins = 0
font = pygame.font.SysFont('Verdana', 60)
font_score = pygame.font.SysFont('Verdana', 20)
font_coin = pygame.font.SysFont('Verdana', 20)
game_over_ = pygame.image.load('game_over.png')
game_over = pygame.transform.scale(game_over_, (400, 600))
background_music = pygame.mixer.music.load('background.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

background = pygame.image.load('AnimatedStreet.png')

screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)

pygame.display.set_caption('Racer')

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width_ - 40), 0)   
    
    def move(self):
        global coins
        self.rect.move_ip(0, speed)
        if pygame.sprite.spritecollideany(P1, gold):
            self.rect.top = 0
            self.rect.center = (random.randint(15, width_ - 15), 0)
            coins += 1
            pygame.mixer.Sound('coin.mp3').play()
            
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(15, width_ - 15), 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width_  - 40), 0)
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width_ - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png') 
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] and self.rect.centery > 30:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] and self.rect.centery < 570:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.center > (23, 0):
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.center < (377, 0):
            self.rect.move_ip(5, 0)



P1 = Player()
E1 = Enemy()
C = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
gold = pygame.sprite.Group()
gold.add(C)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.3
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    screen.blit(background, (0 ,0))
    scores = font_score.render(f'Cars: {score}', True, BLACK)
    screen.blit(scores, (10, 10))
    coin = font_coin.render(f'Coins: {coins}', True, BLACK)
    screen.blit(coin, (290, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()


    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        screen.fill((226, 248, 236))
        screen.blit(game_over, (0,0))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3/2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(fps)