import pygame
from configuracoes import *
from jogador import Jogador


class Level:
    """Classe responsável pela configuração do level."""
    def __init__(self):
        # Obter a superfície para o display
        self.superficie = pygame.display.get_surface()

        # Grupos sprites
        self.todos_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        """Função responsável pela configuração do level."""
        self.jogador = Jogador((500, 325), self.todos_sprites)

    def executar(self, delta):
        """Função responsável por executar o level do jogo."""
        self.superficie.fill('black')
        self.todos_sprites.draw(self.superficie)
        self.todos_sprites.update(delta)
