import pygame as pg
from sprites2 import *

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

        #self.crash_sound = pg.mixer.Sound("pling.wav") # laster inn lyd, klar til bruk

        # lager font/teksttype med størrelse 30
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bg = pg.image.load("background.png").convert_alpha()
        self.bg_width = self.bg.get_width()
        self.clock = pg.time.Clock()

        self.new()
    0
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectiles_grp = pg.sprite.Group()
        self.blocks_grp = pg.sprite.Group()

        self.my_player = Player(self) 
   
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
        self.all_sprites.update()
        
        #self.hits = pg.sprite.spritecollide(self.my_player, self.enemies, True)
        self.hits2 = pg.sprite.groupcollide(self.projectiles_grp, self.enemies, True, True)

        # spawn enemies max 10
        while len(self.enemies) < 10:
            self.freak = Enemy()
            self.all_sprites.add(self.freak)
            self.enemies.add(self.freak)


    def draw(self):
        # tegner ting til skjerm på valgt posisjon, og størrelse
        self.screen.blit(self.bg,(self.i,0))
        
        self.screen.blit(self.bg,(self.bg_width+self.i,0))
        if (self.i==-self.bg_width):
            self.screen.blit(self.bg,(self.bg_width+self.i,0))
            self.i=0
        self.i-=1

        self.all_sprites.draw(self.screen)
        self.my_player.draw_energy(self.screen)

        # rendrer/generer teksten som vi kan tegne til game screen
        # dette viser ikke teksten enda, men har bare laget den klar
        self.text_player_hp = self.comic_sans30.render("HP: " + str(self.my_player.hp), False, (RED))
        self.player_energy = self.comic_sans30.render("Energy: " + str(self.my_player.energy), False, (RED))
        
        # tegn teksten til skjermen på en satt posisjon
        self.screen.blit(self.text_player_hp, (10, 10))
        self.screen.blit(self.player_energy, (10, 40))

        # oppdaterer alle endringer på spill vinduet
        pg.display.update()

g = Game()

