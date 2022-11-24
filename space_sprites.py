import pygame as pg
vec = pg.math.Vector2
from random import randint

pg.init()
pg.mixer.init()

enemy_image = pg.image.load("img/enemy.png")
player_image = pg.image.load("img/player.png")
small_attack_image = pg.image.load("img/fireball.png")
big_attack_image = pg.image.load("img/big_fireball.png")

small_attack_sound = pg.mixer.Sound("sounds/shoot_fire.wav")


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = player_image
        self.image = pg.transform.scale(self.image, (125,75))
        self.rect = self.image.get_rect()
        self.pos = vec(100, 100)
        self.rect.center = self.pos

        self.energy = 100
        self.max_energy = 100
        self.small_attack_cost = 10
        self.big_attack_cost = 50

        self.last_attack = 0
        self.attack_interval = 500

        self.speed = 3
        self.hp = 150

    
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed        

        mouse = pg.mouse.get_pressed()
        
        if mouse[0]: # 0 er venstre klikk, 1 middle, 2 høyreklikk
            self.attack()
        if mouse[2]:
            self.big_attack()

        self.rect.center = self.pos
       

        if self.energy < self.max_energy:
            self.energy += 1
       
    def attack(self):
        now = pg.time.get_ticks()
        if self.energy > self.small_attack_cost and now - self.last_attack > self.attack_interval:
            print("attacked")
            self.energy -= self.small_attack_cost
            self.last_attack = pg.time.get_ticks()
            Ranged_attack(self.game, "small")
            pg.mixer.Sound.play(small_attack_sound)

    def big_attack(self):
        now = pg.time.get_ticks()
        if self.energy > self.big_attack_cost and now - self.last_attack > self.attack_interval:
            self.energy -= self.big_attack_cost
            self.last_attack = pg.time.get_ticks()
            Ranged_attack(self.game, "big")
            pg.mixer.Sound.play(small_attack_sound)

    def draw_bar(self, surf, pos, size, borderC, backC, healthC, progress):
        pg.draw.rect(surf, backC, (*pos, *size))
        pg.draw.rect(surf, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+1, pos[1]+1)
        innerSize = ((size[0]-2) * progress, size[1]-2)
        rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
        pg.draw.rect(surf, healthC, rect)

    def draw_energy(self, surf):
        energy_rect = pg.Rect(0, 0, self.image.get_width(), 7)
        energy_rect.center = vec(75,80)
      
        topleft = energy_rect.bottomleft
        bar_size = energy_rect.size
        self.draw_bar(surf, topleft, bar_size, (0, 0, 0), (255, 0, 0), (0, 255, 0), self.energy/self.max_energy)


class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, type):
        self.groups = game.all_sprites, game.projectiles_grp
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if type == "small":
            self.image = small_attack_image
        elif type == "big":
            self.image = big_attack_image
            self.big = True

        self.orig_image = self.image

        self.rect = self.image.get_rect()
        self.pos = vec(game.player.pos.x + 50 + self.image.get_width(),game.player.pos.y)
        self.rect.center = self.pos
        self.speed = 10
        self.angle = 0
        
        self.attack_to = vec(pg.mouse.get_pos())
        self.attack_direction = self.attack_to - self.pos  # finner "forskjellen" mellom self.pos og posisjon til musepeker
        self.direction = self.attack_direction.normalize() * self.speed  

        print(self.game.projectiles_grp)
        print(self.rect)


    def update(self):
        self.pos += self.direction
        self.rect.center = self.pos
        self.angle += 10
       

        self.image, self.rect = self.rot_center(self.orig_image, self.angle, self.pos.x, self.pos.y)
       

    def rot_center(self, image, angle, x, y):   
        rotated_image = pg.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

        return rotated_image, new_rect
       

class Enemy(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos = vec(randint(500,600), randint(0, 600)) # start posisjon
        self.rect.center = self.pos
        self.speed_x = 4
        self.life = 50
        self.knockbacked = False
        self.knock_time = 0
        self.direction = 0
    
    def update(self):

        if self.pos.x < -100:
            self.kill()
        
        now = pg.time.get_ticks()

        if self.knockbacked:
            if self.knock_time + 1000 < now:
                print("knockback over")
                self.knockbacked = False
                self.speed_x = 4
        
            #print("knockbacked")
            #print(self.direction)
            self.pos += self.direction
        

        self.pos.x += -self.speed_x

        self.rect.center = self.pos

    def knockback(self, player_pos, hit_pos):
        if not self.knockbacked:
            self.knockbacked = True
            self.player_hit_pos = player_pos
            self.knock_time = self.game.now
            #self.speed_x = 0
            knock_pos = vec(hit_pos)
            knock_vec = knock_pos - self.player_hit_pos
            self.direction = knock_vec.normalize() * 3

        
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

