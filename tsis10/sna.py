import pygame
from random import randrange

size = width, height = 1050, 650
block = 25

x, y = randrange(0, width, block), randrange(0, height, block)
food = randrange(0, width, block), randrange(0, height, block)
dirs = {'W':True, 'S':True, 'A':True, 'D':True}
lenght = 1
score = 0
level = 1
snake = [(x, y)]
dx ,dy = 0, 0
fps = 10

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_background = pygame.transform.scale(pygame.image.load('grass.jpg'), (1050, 650))
font_score = pygame.font.SysFont('Arial', 26, bold =True)
fond_end = pygame.font.SysFont('Arial', 66, bold = True)
font_level = pygame.font.SysFont('Arial', 26, bold = True)

while True:
    screen.blit(game_background, (0,0))
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block -1, block - 1 ))
    pygame.draw.rect(screen, pygame.Color('red'), (*food, block, block))

    #snake Score and level
    render_score = font_score.render(f'Score: {score}', True, pygame.Color('orange'))
    screen.blit(render_score,(5 ,5))
    render_level = font_level.render(f'Level: {level}', True, pygame.Color('orange'))
    screen.blit(render_level, (950, 5))

    #snake moving
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-lenght:]

    #game over
    if x < 0 or x > width - block or y < 0 or y > height - block or len(snake) > len(set(snake)):
        while True:
            render_end = fond_end.render('GAME OVER', True, pygame.Color('orange'))
            screen.blit(render_end,(335, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    #eating food
    if snake[-1] == food:
        while food in snake:
            food = randrange(0, width, block), randrange(0, height, block) 
        lenght += 1
        score += 1
        if not score % 10:
            fps += 3
            level += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

    #controll
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and dirs['W']:
        dx, dy = 0, -1   
        dirs = {'W': True, 'S': False, 'A':True, 'D':True}
    if key[pygame.K_DOWN] and dirs['S']:
        dx , dy = 0 , 1
        dirs = {'W':False, 'S':True, 'A': True, 'D':True}
    if key[pygame.K_LEFT] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W':True, 'S':True, 'A': True, 'D':False}
    if key[pygame.K_RIGHT] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W':True, 'S':True, 'A': False, 'D':True}