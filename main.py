import sys
import pygame
from level import Level
from configuracoes import *


class Jogo:
    """Classe resposnsável por carregar o jogo."""
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('PyDew Valley')
        self.relogio = pygame.time.Clock()
        self.level = Level()

    def executar(self):
        """Função responsável por executar o jogo."""
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            delta = self.relogio.tick() / 1000
            self.level.executar(delta)
            pygame.display.update()


if __name__ == '__main__':
    jogo = Jogo()
    jogo.executar()
