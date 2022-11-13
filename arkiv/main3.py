import pygame as pg
pg.init()
 
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
screen = pg.display.set_mode((800,600))

player_img = pg.image.load("player.png")
player_img = pg.transform.scale(player_img,(100,100))
 
x = 50
y = 50

playing = True
while playing: # game loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        y -= 1
    if keys[pg.K_s]:
        y += 1
    if keys[pg.K_a]:
        x -= 1
    if keys[pg.K_d]:
        x += 1


    if x > 700:
        x = 700
    if x < 0:
        x = 0
    if y > 500:
        y = 500
    if y < 0:
        y = 0

    # tegne bakgrunn
    screen.fill(BLACK)
    
    screen.blit(player_img,(x, y))

    pg.display.update()