import pygame
import sys
from pygame.locals import *
from Logica import *
from fabricas import *

class Modelo():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((500,500))
        pygame.display.set_caption("Animacion")
        self.background_image= util().cargar_imagen("Imagenes/fondo.jpg")
        self.director= Director()
        self.director.set_builder(ConstructorPersonaje(FabricaBomberman()))
        self.Bomber=self.director.Get_personaje()
        self.Bomber.Move_Right()
        self.teclas=None
        self.ejecuntado=True
        self.Ventana()
  
    def Dibujar(self):
        self.teclas=pygame.key.get_pressed()
        if self.teclas[K_RIGHT]:
                self.Bomber.Move_Right()
                self.screen.blit(self.Bomber.Get_ImageAc(),(self.Bomber.Get_posx(),140))
        elif self.teclas[K_LEFT]:
                self.Bomber.Move_Left()
                self.screen.blit(self.Bomber.Get_ImageAc(),(self.Bomber.Get_posx(),140))
        else:
            imagen=util().cargar_imagen("Imagenes/11.gif")        
            self.screen.blit(imagen,(self.Bomber.Get_posx(),140))        

    def Ventana(self):
        while self.ejecuntado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ejecuntado=False
                    sys.exit() 
            self.screen.blit(self.background_image,(0,0))
            self.Dibujar()
            pygame.display.update()
            pygame.time.delay(50)        


class util():
    def cargar_imagen(self,nombre):
        image=pygame.image.load(nombre)
        return image.convert()





if __name__ == "__main__":
    Modelo()