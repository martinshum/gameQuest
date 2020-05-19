# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# source code from in class with Mr. Cozort and KidsCanCode 
# Player sprite and movement
import pygame as pg
from pygame.sprite import Sprite
import random
from os import path

# screen dimensions and fps
WIDTH = 480
HEIGHT = 600
FPS = 60
# variables
score = 0
ammo = 100
# define colors
WHITE = (255, 255, 255)
DARKBLUE = (39, 54, 77)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
game_dir = path.join(path.dirname(__file__))

# load all images here - background, player, mobs, lazer
background_image = pg.image.load(game_dir + "/img/bg.png")
# two backgrounds for scrolling screen
background_rect = background_image.get_rect()
background_rect2 = background_image.get_rect()
player_image = pg.image.load(game_dir + "/img/player.png")
mob_image = pg.image.load(game_dir + "/img/mob.png")
freeze_image = pg.image.load(game_dir + "/img/freeze.png")
spit_img = pg.image.load(path.join(game_dir + "/img/spit.png"))

# initialize pygame...
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Crusaders")
clock = pg.time.Clock()

# utils
font_name = pg.font.match_font('arial')
# this is for draw texts that i used for ammo and socre
def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (int(x), int(y))
    surf.blit(text_surface, text_rect)

# shield bar for each of the players player 1 in top left and player 2 in top right
def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(surf, GREEN, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

# player class which is all the details of player 1 
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.transform.scale(player_image, (50, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 10
        self.shield = 100
        self.hitpoints = 100
        self.ammo = ammo
    def update(self):
        self.speedx = 0
        # self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE]:
            self.pew()
        if keystate[pg.K_a]:
            self.speedx = -8
        if keystate[pg.K_d]:
            self.speedx = 8
        # if keystate[pg.K_w]:
        #     self.speedy = -8
        # if keystate[pg.K_s]:
        #     self.speedy = 8
        self.rect.x += self.speedx
        # self.rect.y += self.speedy
        # while running:
        #     if self.ammo == 0:
        #         running = False
# this uses the lazer class to make this a function of the player class
    def pew(self):
        if self.ammo > 0:
            lazer = Lazer(self.rect.centerx, self.rect.top)
            all_sprites.add(lazer)
            lazers.add(lazer)
            self.ammo -=1

# same details as player 1 but for player 2 and different controls. 
class Player2(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.transform.scale(player_image, (50, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 10
        self.shield = 100
        self.hitpoints = 100
        self.ammo = ammo
    def update(self):
        self.speedx = 0
        # self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE]:
            self.pew()
        if keystate[pg.K_LEFT]:
            self.speedx = -8
        if keystate[pg.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
# this uses the lazer class to make this a function of the player class
    def pew(self):
        if self.ammo > 0:
            lazer = Lazer(self.rect.centerx, self.rect.top)
            all_sprites.add(lazer)
            lazers.add(lazer)
            self.ammo -=1
# mob class sprite 
class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.transform.scale(mob_image, (40, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(0, 240)
        self.speedx = random.randrange(1,10)
        self.speedy = random.randrange(0, 10)
    def pew(self):
        spit = Spit(self.rect.centerx, self.rect.top)
        all_sprites.add(spit)
        spits.add(spit)
        # print('trying to shoot..')
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.speedx*=-1
            self.rect.y += 25
        if random.random() > 0.99:
            self.pew()
        if self.rect.y > HEIGHT:
            self.rect.y = -25
            self.rect.x = random.randrange(0, WIDTH-self.rect.width)
# freezes the mobs when the player's shield is gone
        if player.shield == 0:
            self.speedx = 0
        if player2.shield == 0:
            self.speedx = 0
# lazer class that creates the lazer used in the players
class Lazer(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((5,25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
# creates the mobs weappon which they spit down on players
class Spit(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = spit_img
        # self.image = pg.Surface((5,10))
        # self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.y < 0:
            self.kill()
# creates a bigger spit ball and makes it hader for the player to dodge based on the score of the player
        if score > 1000:
            self.image = pg.transform.scale(spit_img, (40, 40))
        if score > 2000
            self.image = pg.transform.scale(spit_img, (50, 50))
            # print(len(lazers))
# where all the new things are created for the game
all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
lazers = pg.sprite.Group()
player = Player()
player2 = Player2()
spits = pg.sprite.Group()
all_sprites.add(player)
freezes = pg.sprite.Group()
# lazer = Lazer(player.rect.x, player.rect.y)
# all_sprites.add(lazer)
# this summons the mobs and if you change the range you can add or subtract mods

# creates the first of the mobs / 3 of them
for i in range(0,3):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)

# the game loop
running = True
while running: 
    # keep loop running based on clock
    clock.tick(FPS)
    for event in pg.event.get():
        # window x button
        if event.type == pg.QUIT:
            running = False

    # update all the sprites
    all_sprites.update()
    # this checks for collissions and when mobs and lazers hit both are gone
    hits = pg.sprite.groupcollide(mobs, lazers, True, True)
    # adds a score and ammo for each enemy killed
    if hits:
        score += 100
        player.ammo +=100
        player2.ammo +=100
# takes away shield from player 1 or player 2 if they are hit with a spit from the mob
    hits = pg.sprite.spritecollide(player, spits, False)
    if hits:
        player.shield -= 5
    hits = pg.sprite.spritecollide(player2, spits, False)
    if hits:
        player2.shield -= 5
# adds in player 2 when the score equals 1000
    if score == 1000:
        all_sprites.add(player2)


# when a mob hits the player the if statement makes the game stop
    hits = pg.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
# when all the mobs are gone spawn more mobs in 8 this time
    if len(mobs) == 0:
        for i in range(0,8):
            mob = Mob()
            all_sprites.add(mob)
            mobs.add(mob)
# creates a scrolling background
    background_rect2.y = background_rect.y - 600
    background_rect.y += player.speedy
    background_rect2.y += player.speedy
# swaps the background 1 with background 2 which makes the scrolling background
    if background_rect2.y >- 0:
        background_rect.y = background_rect.y -600

    # Draw
    screen.fill(DARKBLUE)
    screen.blit(background_image, background_rect)
    screen.blit(background_image, background_rect2)
    draw_text(screen, str(score), 24, WIDTH / 2, 10)
    draw_text(screen, str(player.ammo), 24, WIDTH / 4, 10)
    draw_text(screen, str(player.hitpoints), 16, player.rect.x, player.rect.y)
    draw_shield_bar(screen, 5, 5, player.shield)
    # this creates the shield bar for player 2
    if score > 1000:
        draw_shield_bar(screen, 380, 5, player2.shield)
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()