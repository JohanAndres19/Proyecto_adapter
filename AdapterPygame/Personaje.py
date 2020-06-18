import pygame
from pygame import *
from .prueba import *

class Character(pygame.sprite.Sprite):

    def __init__(self):
        self.velocity = 10
        self.image = None
        self.dir = 0
        self.images = []
        self.current = 0

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def update(self):
        self.image = self.images[self.dir][self.current]
        self.current +=1
        self.current %= len(self.images[self.dir])
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def place(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def setImages(self, sprites):
        pass


class mainCharacter(Character):

    sprites = [
                ['AdapterPygame/static/R0.png', 'AdapterPygame/static/R1.png', 'AdapterPygame/static/R2.png', 'AdapterPygame/static/R3.png',
                 'AdapterPygame/static/R4.png', 'AdapterPygame/static/R5.png'],
                ['AdapterPygame/static/L0.png', 'AdapterPygame/static/L1.png', 'AdapterPygame/static/L2.png', 'AdapterPygame/static/L3.png', 
                 'AdapterPygame/static/L4.png', 'AdapterPygame/static/L5.png']
                                                                                    ]

    def __init__(self):
        Character.__init__(self)
        self.setImages(self.sprites)
        
    def moveRight(self):
        self.rect.left += self.velocity
        self.dir = 0
        self.update()

    def moveLeft(self):
        self.rect.left -= self.velocity
        self.dir = 1
        self.update()

    def setImages(self, sprites):
        self.images = loadImages(sprites)
        self.image = self.images[self.dir][self.current]
        self.rect = self.image.get_rect()
