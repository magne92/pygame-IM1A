import pygame as pg
vec = pg.math.Vector2
from random import randint

enemy_image = pg.image.load("pygame\enemy.png")
player_image = pg.image.load("pygame\player.png")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (125,75))
        self.rect = self.image.get_rect()
        self.pos = vec(100, 100)
        self.rect.center = self.pos
        self.speed = 3
        self.hp = 150
    
    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed

        self.rect.center = self.pos

        '''
         # hvis helt til høyre
        if ting_pos_x + ting_size_x > WIDTH:
            ting_pos_x = WIDTH - ting_size_x
        # hvis helt til venstre
        if ting_pos_x < 0:
            ting_pos_x = 0
        # opp og ned
        if ting_pos_y < 0:
            ting_pos_y = 0        
        if ting_pos_y + ting_size_y > HEIGHT:
            ting_pos_y = HEIGHT - ting_size_y
        '''



class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos = vec(1000, randint(0, 600)) # start posisjon
        self.rect.center = self.pos
        self.speed_x = 1
        self.life = 50
    
    def update(self):
        self.pos.x += self.speed_x

        if self.pos.x > 800: # hvis til høyre for skjerm
            self.speed_x = -1
        if self.pos.x < 0: # hvis til venstre for skjerm
            self.speed_x = 1

        self.rect.center = self.pos

