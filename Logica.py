class Director():
    _Builder=None

    def set_builder(self,builder):
       self._Builder=builder

    def Get_personaje(self):
        bomber=Bomberman()
        bomber.Set_imagenes(self._Builder.Get_sprites())
        return bomber

    

class ConstructorPersonaje():
    def __init__(self,fabrica):
        self.fabrica=fabrica

    def Get_sprites(self):
        return[self.fabrica.Mover_derecha(),
               self.fabrica.Mover_izqui()]   

class Bomberman():
     
    def __init__(self):
        self.posx=0
        self.imagenes=[]
        self.imageAc=None
        self.contador =0     

    def Set_imagenes(self,imagenes):
        self.imagenes=imagenes

    def Get_imagenes(self):
        return self.imagenes        

    def Move_Right(self):
        if self.contador==0:
            self.posx=self.posx+5
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=1
        elif self.contador==1:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=2
        elif self.contador==2:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=3
        elif self.contador==3:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=4
        elif self.contador==4:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=0        

    def Move_Left(self):
        if self.contador==0:
            self.posx=self.posx-5
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=1
        elif self.contador==1:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=2
        elif self.contador==2:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=3
        elif self.contador==3:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=4
        elif self.contador==4:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=0    

    def Get_ImageAc(self):
        return self.imageAc

    def Set_ImageAc(self,imagen):
        self.imageAc=imagen
    
    def Get_posx(self):
        return self.posx












