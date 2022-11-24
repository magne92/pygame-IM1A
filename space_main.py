import pygame as pg
from space_sprites import *

WIDTH = 1024
HEIGHT = 600
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Game():
    def __init__(self):
        pg.init()
        pg.mixer.init()

        
        pg.mixer.music.load("sounds/bgm_0.mp3")
      
        #self.crash_sound = pg.mixer.Sound("pling.wav") # laster inn lyd, klar til bruk

        # lager font/teksttype med størrelse 30
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bg = pg.image.load("img/background.png").convert_alpha()
        self.bg_width = self.bg.get_width()
        self.clock = pg.time.Clock()

        self.new()

    def new(self):
        pg.mixer.music.play(-1)
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectiles_grp = pg.sprite.Group()
        self.blocks_grp = pg.sprite.Group()

        self.player = Player(self) 
   
        self.i = 0
        self.run()

    def run(self):
        self.playing = True
        while self.playing: # game loop
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        self.new()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.playing = False
                            
    def update(self):
        self.now = pg.time.get_ticks()
        self.all_sprites.update()
        
        hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            # knockback when collided          
            for enemy in hits:
                enemy.knockback(self.player.pos, enemy.pos)

        '''
        if hits:
            # knockback when collided
            knock_pos = vec(hits[0].pos)
            knock_vec = knock_pos - self.player.pos 
            self.player.pos -= knock_vec.normalize() * 100
        '''
        self.hits2 = pg.sprite.groupcollide(self.projectiles_grp, self.enemies, True, True)

        # spawn enemies max 10
        while len(self.enemies) < 10:
            self.enemy = Enemy(self)
            self.all_sprites.add(self.enemy)
            self.enemies.add(self.enemy)


    def draw(self):
        # tegner ting til skjerm på valgt posisjon, og størrelse
        self.screen.blit(self.bg,(self.i,0))
        
        self.screen.blit(self.bg,(self.bg_width+self.i,0))
        if (self.i==-self.bg_width):
            self.screen.blit(self.bg,(self.bg_width+self.i,0))
            self.i=0
        self.i-=1

        self.all_sprites.draw(self.screen)
        self.player.draw_energy(self.screen)

        # rendrer/generer teksten som vi kan tegne til game screen
        # dette viser ikke teksten enda, men har bare laget den klar
        self.text_player_hp = self.comic_sans30.render("HP: " + str(self.player.hp), False, (RED))
        self.player_energy = self.comic_sans30.render("Energy: " + str(self.player.energy), False, (RED))
        
        # tegn teksten til skjermen på en satt posisjon
        self.screen.blit(self.text_player_hp, (10, 10))
        self.screen.blit(self.player_energy, (10, 40))

        # oppdaterer alle endringer på spill vinduet
        pg.display.update()

    def level(self):
        pass

g = Game()

