import pygame
import os
from os import path
from settings import *
from sprites import *

class Game():
    def __init__(self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.ladders = pygame.sprite.Group()
        
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40, GREEN)
        p2 = Platform(WIDTH / 2 - 50, HEIGHT / 4, 100, 10, GREEN)
        L1 = Platform(50, HEIGHT - 500, 50, 460, BROWN)
        self.all_sprites.add(p1)
        self.all_sprites.add(p2)
        self.all_sprites.add(L1)
        self.platforms.add(p1)
        self.platforms.add(p2)
        self.ladders.add(L1)
                
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS) 
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        keys = pygame.key.get_pressed()
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.falling = False
            self.player.pos.y = hits[0].rect.top + 1
            self.player.vel.y = 0

    def events(self):
        # game loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.climb()

    def draw(self):
        # game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        pass

g = Game()
while g.running:
    g.new()

pygame.quit()
quit()
