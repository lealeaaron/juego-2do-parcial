from configuraciones import *
from class_enemigo import *
class Personaje:
    def __init__(self, animaciones, pos_x, pos_y, tamaño, velocidad, que_hace):
        
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo = pygame.Rect(pos_x, pos_y, *tamaño)
        #self.rectangulo = self.animaciones["quieto"][0].get.rect
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.velocidad = velocidad
        
        self.que_hace = que_hace
        self.contador_pasos = 0

        self.animacion_actual = self.animaciones[self.que_hace]

        self.gravedad = 1
        self.desplazamiento_y = 0
        self.potencia_salto = -10
        self.limite_velocidad_salto = 10
        self.esta_saltando = False
    

    def aplicar_gravedad(self,pantalla, lista_plataformas):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

            for plataforma in lista_plataformas:
                if self.rectangulo.colliderect(plataforma["rectangulo"]):
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                    self.rectangulo.bottom = plataforma["rectangulo"].top

    @staticmethod
    def metodo_estatico():
        pass


    def desplazar(self):
        velocidad_actual = self.velocidad
        if self.que_hace == "izquierda":
            velocidad_actual *= -1
        self.rectangulo.x += velocidad_actual


    def animar(self,pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        

        pantalla.blit(self.animacion_actual[self.contador_pasos],self.rectangulo)
        self.contador_pasos += 1

    def actualizar(self, pantalla, lista_plataformas):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["derecha"]
                    self.animar(pantalla)
                self.desplazar()
            case "izquierda":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["izquierda"]
                    self.animar(pantalla)
                self.desplazar()
            case "quieto":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["quieto"]
                    self.animar(pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.animaciones["salta"]
        

        self.aplicar_gravedad(pantalla, lista_plataformas)

    
    def verificar_colision_enemigo(self, enemigo:Enemigo):
        if self.rectangulo.colliderect(enemigo.rectangulo):
            enemigo.esta_muerto = True