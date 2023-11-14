from configuraciones import *
from class_personaje import *
from pygame.locals import *
from class_enemigo import *
from modo import *
import sys

def crear_plataforma(es_visible, tamaño, posicion, path = "" ) -> dict:
    plataforma = {}
    if es_visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = pygame.Surface(tamaño)
    
    plataforma["rectangulo"] = plataforma["superficie"].get_rect()

    x, y = posicion

    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y

    return plataforma

##############################INICIALIZACIONES##########################################

#############Pantalla##########
ANCHO, ALTO = 1600 , 900
FPS = 18 #para desacelerar la pantalla

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO, ALTO)) # en pixeles

#Fondo
fondo = pygame.image.load(r"Recursos\fondo.jpg")#Acelera el juego y hace que consuma menos recursos
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO)) 

#Personaje
diccionario_animaciones = {}
diccionario_animaciones["derecha"] = personaje_derecha
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["izquierda"] = personaje_izquierda
diccionario_animaciones["salta"] = personaje_salta

mario = Personaje(diccionario_animaciones,500,160,(70,60),10, "quieto")

piso = crear_plataforma(False, (ANCHO,20), (0,825))

plataforma_caño = crear_plataforma(True, (150,150), (1290,700), "Recursos\Caño.png")

lista_plataformas = [piso,plataforma_caño]

mario.rectangulo.bottom = piso["rectangulo"].top

##################################################
#ENEMIGO

diccionario_animaciones_enemigo = {"izquierda": enemigo_camina, "aplastado": enemigo_aplastado }
un_enemigo =  Enemigo(diccionario_animaciones_enemigo)

un_enemigo.rectangulo.bottom = piso["rectangulo"].top

lista_enemigos = [un_enemigo]

bandera = True
while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            bandera = False
        elif evento.type == KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == MOUSEBUTTONDOWN:
            print(evento.pos)
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        mario.que_hace = "derecha"
    elif teclas[pygame.K_LEFT]:
        mario.que_hace = "izquierda"
    elif teclas[pygame.K_UP]:
        mario.que_hace = "salta"
    else:
        mario.que_hace = "quieto"


    PANTALLA.blit(fondo,(0,0))

    mario.actualizar(PANTALLA,lista_plataformas)
    Personaje.metodo_estatico()
    PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"])

    un_enemigo.actualizar(PANTALLA)
    
    mario.verificar_colision_enemigo(un_enemigo)
    
    for enemigo in lista_enemigos:
        if enemigo.esta_muerto:
            del enemigo

    if obtener_modo():
        pygame.draw.rect(PANTALLA, "pink", mario.rectangulo, 3)
        for enemigo in lista_enemigos:
            if not enemigo.esta_muerto:
                pygame.draw.rect(PANTALLA, "red",plataforma["rectangulo"] , 3)

    pygame.display.update()

pygame.quit()


