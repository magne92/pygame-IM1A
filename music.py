import pygame as pg

class Game():
    def __init__(self):
        pg.init()

        pg.mixer.music.load('musikk.wav') # laster inn musikk, klar til bruk, .wav, .mp3 og .ogg filer støttes

        self.spawn_sound = pg.mixer.Sound("pling.wav") # laster inn en enkelt lydeffekt, 

    def new(self):
        pg.mixer.music.play(-1)  # starter musikken som er lastet inn, -1 betyr at den aldri stopper


    def update(self):
            self.all_sprites.update()
            # spawn enemies max 10
            while len(self.enemies) < 10:
                self.freak = Enemy()
                self.all_sprites.add(self.freak)
                self.enemies.add(self.freak)
                pg.mixer.Sound.play(self.spawn_sound)


            # her velger vi å spille av en lyd når en ny enemy lages. 
            
            # om du ønsker å spille av lyd ved angrep, fiende dør osv:
            # Plasser pg.mixer.Sound.play(self.sound) i sprite filen, feks inni attack funksjon