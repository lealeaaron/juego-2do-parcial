from configuraciones import *

class Enemigo:
    def __init__(self, animaciones):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, (50,50))
        #self.rectangulo = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo = pygame.Rect(1200,610,50,50)
        self.contador_pasos = 0

        self.animacion_actual = self.animaciones["izquierda"]

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

    def avanzar(self):
        self.rectangulo.x -= 1
        

    def actualizar(self, pantalla):
        self.animar(pantalla)
        self.avanzar()
