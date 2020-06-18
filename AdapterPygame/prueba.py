import pygame

def loadImages(sprites):
    surfaces = []
    for images in sprites:
        surface = []
        for image in images:
            surface.append(pygame.image.load(image))
        surfaces.append(surface)

    return surfaces