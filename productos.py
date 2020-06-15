import pygame


class AbstractRight():
    def Sprites_ri(self):
        pass

class AbstractLeft():
    def Sprites_le(self):
        pass

class SpriteDerechaBo(AbstractRight):
    def Sprites_ri(self):
        return[pygame.image.load('Imagenes/31.gif'),
               pygame.image.load('Imagenes/32.gif'),
               pygame.image.load('Imagenes/33.gif'),
               pygame.image.load('Imagenes/34.gif'),
               pygame.image.load('Imagenes/35.gif')]    

class SpritesIzquiBo(AbstractLeft):
    def Sprites_le(self):
        return[pygame.image.load('Imagenes/21.gif'),
               pygame.image.load('Imagenes/22.gif'),
               pygame.image.load('Imagenes/23.gif'),
               pygame.image.load('Imagenes/24.gif'),
               pygame.image.load('Imagenes/25.gif')]