from productos import *

class FabricaAbstacta():
    def Mover_derecha(self):
        pass

    def Mover_izqui(self):
        pass

class FabricaBomberman(FabricaAbstacta):    
    def Mover_derecha(self):
        Spritesderecha =SpriteDerechaBo()
        return Spritesderecha.Sprites_ri()
   
    def Mover_izqui(self):
        SpritesIz= SpritesIzquiBo()
        return SpritesIz.Sprites_le()



