import pygame




def girar_imagenes(lista_original, flip_x, flip_y ):
    lista_girada = []
    
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada


def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)

personaje_quieto = [pygame.image.load(r"Recursos\0.png")]

personaje_derecha = [pygame.image.load(r"Recursos\1.png"),
                    pygame.image.load(r"Recursos\2.png")]

personaje_salta = [pygame.image.load(r"Recursos\3.png")]

personaje_izquierda = girar_imagenes(personaje_derecha, True, False)

enemigo_camina = [pygame.image.load(r"Recursos\ene1.png")]

enemigo_aplastado = [pygame.image.load(r"Recursos\ene3.png")]