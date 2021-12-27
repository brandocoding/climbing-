import pygame
import os
from os import path
import math
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 96
        self.pos = vec(WIDTH / 2, HEIGHT - 96)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.falling = False

    def update(self):
        #print(self.pos)      
        self.acc = vec(0, 0.5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pygame.K_DOWN]:
            self.acc.y = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def climb(self):  
        hits = pygame.sprite.spritecollide(self, self.game.ladders, False)
        if hits:
            self.vel.y = -5

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
               
                    
    
