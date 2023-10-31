import pygame
pygame.init()
pygame.font.init()
pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.queue("music2.mp3")
pygame.mixer.music.queue("music3.mp3")
_songs = ["music1.mp3", "music2.mp3", "music3.mp3"]
def next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def previous_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
size = width, height = (800, 200)
screen = pygame.display.set_mode(size)
screen.fill((0,255,255))
pygame.draw.rect(screen, (255,255,255), (50,50,30,100))
pygame.draw.polygon(screen, (255,255,255),[(80,100), (150, 50), (150,150)])
pygame.draw.polygon(screen, (255,255,255),[(250, 50), (250,150), (350, 100)])
pygame.draw.rect(screen, (255,255,255), (450,50,45,100))
pygame.draw.rect(screen,(255,255,255), (505, 50, 45,100))
pygame.draw.polygon(screen, (255,255,255),[(650,50),(650,150), (720,100)])
pygame.draw.rect(screen, (255,255,255),(720,50,30,100))
z = pygame.font.Font(None , 25)
z_ = z.render("press z", False, (0,0,0))
x = pygame.font.Font(None, 25)
x_ = x.render("press x", False, (0,0,0))
c = pygame.font.Font(None , 25)
c_ = c.render("press c", False, (0,0,0))
v = pygame.font.Font(None , 25)
v_ = v.render("press v", False, (0,0,0))
screen.blit(z_, (70,155))
screen.blit(x_, (270,155))
screen.blit(c_, (470,155))
screen.blit(v_, (670,155))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            next_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            previous_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.unpause()
    pygame.display.flip()
pygame.quit()