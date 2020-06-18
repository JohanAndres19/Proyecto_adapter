import pygame
import sys
from pygame.locals import *
from Logica import *
from fabricas import *

class Modelo():
    # constructor  Inicializa la ventana y el director para poder obtener el personaje que 
    # se solicite
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((500,500))
        pygame.display.set_caption("Animacion")
        self.background_image= util().cargar_imagen("Imagenes/fondo1.jpg")
        self.screen.blit(self.background_image,(0,0))
        self.director = Director()
        self.personaje=None
        self.ejecuntado=True
        self.vivo=False
        self.Boton_presionado=0
        self.Ventana()
  # metodo que dibuja el personaje que se selecciona y lo anima 
    def Dibujar(self):
        self.teclas=pygame.key.get_pressed()
        if self.teclas[K_b] and self.Boton_presionado==0:
            self.director.set_builder(ConstructorPersonaje(FabricaBomberman()))
            self.personaje=self.director.Get_personaje(1)
            self.vivo=True
            self.Boton_presionado=1
            self.background_image=util().cargar_imagen("Imagenes/fondo.png")
        elif self.teclas[K_d] and self.Boton_presionado==0:
            self.personaje=self.director.Get_personaje(0)
            self.vivo=True
            self.Boton_presionado=1
            self.background_image=util().cargar_imagen("Imagenes/fondo.png")
        elif self.teclas[K_ESCAPE] and self.Boton_presionado==1:
            self.Boton_presionado=0
            self.vivo=False
            self.background_image= util().cargar_imagen("Imagenes/fondo1.jpg")

        if self.vivo==True:    
            self.screen.blit(self.background_image,(0,0))
            if self.teclas[K_RIGHT]:
                    self.personaje.Move_Right()
                    self.personaje.Dibujar(self.screen)
            elif self.teclas[K_LEFT]:
                    self.personaje.Move_Left()
                    self.personaje.Dibujar(self.screen)
            else:
                pass       
                self.personaje.Detener(self.screen)        
        else:
            self.screen.blit(self.background_image,(0,0))
    
    # metodo que mantiene la ventana activa y realiza la llamada continua del metodo dibujar  
    def Ventana(self):
        while self.ejecuntado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ejecuntado=False
                    sys.exit() 
            self.Dibujar()
            pygame.display.update()
            pygame.time.delay(100)        




if __name__ == "__main__":
    Modelo()