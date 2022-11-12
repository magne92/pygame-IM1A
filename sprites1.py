import pygame as pg
import math
vec = pg.math.Vector2
from random import randint

enemy_image = pg.image.load("enemy.png")
player_image = pg.image.load("player.png")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (125,75))
        self.rect = self.image.get_rect()
        self.pos = vec(400, 400)
        self.rect.center = self.pos
        self.move_speed = 0
        self.speed_x = 0
        self.speed_y = 0
        self.hp = 150
        self.speed = 5

        self.can_move_up, self.can_move_down, self.can_move_right, self.can_move_left = True,True,True,True

    
    def update(self):
        keys = pg.key.get_pressed()
        self.speed_x = 0
        self.speed_y = 0
        '''
        if keys[pg.K_w] and self.can_move_up:           
            self.pos.y -= self.move_speed
        if keys[pg.K_s] and self.can_move_down:
            self.pos.y += self.move_speed
        if keys[pg.K_a] and self.can_move_left:
            self.pos.x -= self.move_speed
        if keys[pg.K_d] and self.can_move_right:
            self.pos.x += self.move_speed
        '''
        if keys[pg.K_SPACE]:
            self.pos = vec(100,100)
        if keys[pg.K_w] and self.can_move_up:           
            self.speed_y = -3
        if keys[pg.K_s] and self.can_move_down:
            self.speed_y = 3        
        if keys[pg.K_a] and self.can_move_left:
           self.speed_x = -3
        if keys[pg.K_d] and self.can_move_right:
            self.speed_x = 3
        '''
        self.hit_block = pg.sprite.spritecollide(self, self.game.blocks_grp, False)
        if self.hit_block:
            lowest = self.hit_block[0]
            for hit in self.hit_block:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            if self.rect.bottom > lowest.rect.top:
                self.rect.bottom = lowest.rect.top
                print("colliding bot")

            
            if self.rect.top <= self.hit_block[0].rect.bottom:
                self.speed_y = 0 
                print("colliding top")  

                          
            if self.rect.right >= self.hit_block[0].rect.left:
               self.speed_x = 0  
               print("colliding right")
            if self.rect.left <= self.hit_block[0].rect.right:
                self.speed_x = 0  
                print("colliding left")


        self.angle = vec(self.move_to).angle_to(self.move_to)
        
        self.angle = math.acos.ulp(self.angle)

        self.pos += self.angle
            '''
       
        self.move_to = vec(pg.mouse.get_pos()) # finner posisjon til musepeker
        self.move_vector = self.move_to - self.pos  # finner "forskjellen" mellom self.pos og posisjon til musepeker
        self.pos += self.move_vector.normalize() * self.speed  # flytter self.pos litt mot musepeker
        self.rect.center = self.pos
   
        #self.move_angle = self.pos.normalize() - self.move_to.normalize()
        '''
        dx, dy = (self.pos.x - self.move_to.x, self.pos.y - self.move_to.y)
        self.step_x, self.step_y = (dx / 30, dy / 30)
        self.pos.x -= self.move_to.x * 2
        self.pos.y -= self.move_to.y * 2
        
        self.rect.center = self.pos
        '''
            
        #else:
        #    self.can_move_left, self.can_move_right, self.can_move_down, self.can_move_up = True, True, True, True


        #print(self.can_move_left, self.can_move_right, self.can_move_down, self.can_move_up)
        



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




class Block(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([50,50])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(300, 300) # start posisjon
        self.rect.center = self.pos
    
    
    def update(self):
        self.rect.center = self.pos

