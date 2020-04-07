# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 2
# Video link: https://www.youtube.com/watch?v=8LRI0RLKyt0
# Player movement
# © 2019 KidsCanCode LLC / All rights reserved.

# Week of march 23 - Lore
# Modules, Github, import as, 

import pygame as pg
from pygame.sprite import Group
# from pg.sprite import Sprite
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = Group()
        self.platforms = pg.sprite.Group()
        self.statics = Group()
        self.projectiles = Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ground = Platform(0, HEIGHT-40, WIDTH, 40)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        self.tempGroup = Group()
        # self.all_sprites.add(plat1)
        # self.platforms.add(plat1)
        # self.all_sprites.add(plat2)
        # self.platforms.add(plat2)
        global plat
        for plat in range(1,10):
            plat = Platform(random.randint(15, WIDTH-200), random.randint(100,HEIGHT), random.randint(50,100), 20)
            self.tempGroup.add(plat)
            # for current in self.tempGroup:
            #     platHits = pg.sprite.spritecollide(plat, self.platforms, True)
            #     if platHits:
            #         plat.kill()
            #     else:
            self.all_sprites.add(plat)
            self.platforms.add(plat)       
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        for p in self.projectiles:
            if p.rect.y < 0:
                p.kill
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            if self.player.rect.top > hits[0].rect.top:
            # print("it collided")
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom+5
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top + 1
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    print(len(self.platforms)
    ''' this if statement was working until I changed something in sprite
     i changed the thing back to what it was before but this code is still broken
     if i was to continue with this project I would fix this and add movement'''
        if len(self.platforms) < 8:
            plat = Platform(random.randint(15, WIDTH-200), random.randint(100,HEIGHT), random.randint(50,100), 20)
            self.all_sprites.add(plat)
            self.platforms.add(plat)   
        # if self.platforms
        #     plat = Platform(random.randint(15, WIDTH-200), random.randint(100,HEIGHT), random.randint(50,100), 20)
        #     self.all_sprites.add(plat)
        #     self.platforms.add(plat) 

# this is my attempt to have the platforms check for each other so they do not overlap
# i think i need to potentially assign variables for the platforms so they can check for each other
        # if pg.sprite.spritecollide(self.platforms, self.platforms, False)
        #     plat = Platform(random.randint(15, WIDTH-200), random.randint(100,HEIGHT), random.randint(50,100), 20)
        #     self.all_sprites.add(plat)
        #     self.platforms.add(plat)  
        # generates more platforms as the player moves upwards

    def events(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = FalseG
                self.running = False
    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()
    def show_start_screen(self):
        # game splash/start screen
        pass
    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pg.quit()