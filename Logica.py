from AdapterPygame.Personaje import mainCharacter
import pygame
class Director():
    _Builder=None

    def set_builder(self,builder):
       self._Builder=builder

    def Get_personaje(self,opcion):
        if opcion ==1:
            bomber=Bomberman()
            bomber.Set_imagenes(self._Builder.Get_sprites())
            return bomber
        elif opcion==0:
            character=mainCharacter()
            character.place((0,140))
            adaptado=Adapter(character)
            return adaptado
    

class ConstructorPersonaje():
    def __init__(self,fabrica):
        self.fabrica=fabrica

    def Get_sprites(self):
        return[self.fabrica.Mover_derecha(),
               self.fabrica.Mover_izqui()]   


class Movimiento():
    
    def Move_Right(self):
        pass
    def Move_Left(self):
        pass    
    def Dibujar(self,screen):
        pass
    def Detener(self,screen):
        pass

class Adapter(Movimiento):# clase que adapta los movimientos que se necesitan

    def __init__(self,personaje):
        self._adaptado_=personaje

    def Move_Left(self):
        self._adaptado_.moveLeft()

    def Move_Right(self):
        self._adaptado_.moveRight()

    def Dibujar(self,screen):
        self._adaptado_.draw(screen)

    def Detener(self, screen):
        self._adaptado_.draw(screen)


class Bomberman(Movimiento):
     
    def __init__(self):
        self.posx=0
        self.imagenes=[]
        self.imageAc=None
        self.contador =0  
        self.fila=0  
    
    def Set_imagenes(self,imagenes):
        self.imagenes=imagenes

    def Get_imagenes(self):
        return self.imagenes     
    
    # Actualiza la imagenn corresponiente al movimiento que se realice
    def Actualizar(self):
        self.Set_ImageAc(self.Get_imagenes()[self.fila][self.contador])
        self.contador+=1
        self.contador%=len(self.Get_imagenes()[self.fila])
   
   #cdibuja la imagen correspondiente en la actual posicion
    def Dibujar(self,screen):
        self.screen=screen
        self.screen.blit(self.Get_ImageAc(),(self.Get_posx(),140))

    # dibuja una imagen cunado no hay movimiento en la ultima posicion que este se encuentra    
    def Detener(self, screen):
        self.screen=screen
        imagen=util().cargar_imagen("Imagenes/11.gif")
        self.screen.blit(imagen,(self.Get_posx(),140))
        
    def Move_Right(self):
        self.posx+=5
        self.fila=0
        self.Actualizar()

    def Move_Left(self):
        self.posx-=5
        self.fila=1
        self.Actualizar()

    def Get_ImageAc(self):
        return self.imageAc

    def Set_ImageAc(self,imagen):
        self.imageAc=imagen
    
    def Get_posx(self):
        return self.posx



class util():
    def cargar_imagen(self,nombre):
        image=pygame.image.load(nombre)
        return image.convert()



