import pygame as pg
from sprites import *

pg.init()
#pg.font.init()

WIDTH = 800
HEIGHT = 600

MIDDLE_x_y = (WIDTH/2, HEIGHT/2)

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED= (255,0,0)

# lager font/teksttype med størrelse 30
comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

screen = pg.display.set_mode((WIDTH,HEIGHT))

clock = pg.time.Clock()
FPS = 120

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

freak = Enemy()
all_sprites.add(freak)
enemies.add(freak)

player = Player()
all_sprites.add(player)



playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()

    # tegner ting til skjerm på valgt posisjon, og størrelse
    screen.fill(WHITE)

    # oppdaterer alle sprites
    all_sprites.update()

    # check for collision
    hits = pg.sprite.spritecollide(player, enemies, True) 
    
    # spawn enemies max 10
    while len(enemies) < 10:
        freak = Enemy()
        all_sprites.add(freak)
        enemies.add(freak)


    all_sprites.draw(screen)

    # rendrer/generer teksten som vi kan tegne til game screen
    # dette viser ikke teksten enda, men har bare laget den klar

  

    text_player_hp = comic_sans30.render(str(player.hp), False, (RED))
    
    # tegn teksten til skjermen på en satt posisjon
    screen.blit(text_player_hp, (10, 10))


    pg.display.update()

   
