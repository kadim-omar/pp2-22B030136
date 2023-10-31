import pygame
pygame.init()
size = width, height = (400, 400)
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
ellipse_x = 175
ellipse_y = 175
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if ellipse_y > 12.5:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                ellipse_y -= 20 
        if ellipse_y < 350:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                ellipse_y += 20
        if ellipse_x < 350:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                ellipse_x += 20
        if ellipse_x > 12.5:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                ellipse_x -= 20
    screen.fill((255,255,255))
    pygame.draw.ellipse(screen, (255,0,0) , (ellipse_x, ellipse_y ,50 , 50))
    pygame.display.update()    
pygame.quit()
