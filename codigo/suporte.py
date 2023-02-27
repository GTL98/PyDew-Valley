import pygame
from os import walk


def importar_pasta(caminho: str) -> list:
    """Função responsável por importar as pastas utilizadas no jogo."""
    lista_superficie = []

    for _, __, imagens in walk(caminho):
        for imagem in imagens:
            caminho_completo = f'{caminho}/{imagem}'
            superficie_imagem = pygame.image.load(caminho_completo).convert_alpha()
            lista_superficie.append(superficie_imagem)

    return lista_superficie
