import pygame as pg
from sprites import *

WIDTH = 800
HEIGHT = 600 
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Game():
    def __init__(self):
        pg.init()

        # lager font/teksttype med størrelse 30
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.new()
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()

        self.my_player = Player()
        self.all_sprites.add(self.my_player)

        self.freak = Enemy()
        self.all_sprites.add(self.freak)
        self.enemies.add(self.freak)

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

        self.hits = pg.sprite.spritecollide(self.my_player, self.enemies, True)

        # spawn enemies max 10
        while len(self.enemies) < 10:
            self.freak = Enemy()
            self.all_sprites.add(self.freak)
            self.enemies.add(self.freak)
 

    def draw(self):
        # tegner ting til skjerm på valgt posisjon, og størrelse
        self.screen.fill(WHITE)

        self.all_sprites.draw(self.screen)

        # rendrer/generer teksten som vi kan tegne til game screen
        # dette viser ikke teksten enda, men har bare laget den klar
        self.text_player_hp = self.comic_sans30.render(str(self.my_player.hp), False, (RED))
        
        # tegn teksten til skjermen på en satt posisjon
        self.screen.blit(self.text_player_hp, (10, 10))

        # oppdaterer alle endringer på spill vinduet
        pg.display.update()


g = Game()

