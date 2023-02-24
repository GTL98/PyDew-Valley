import pygame
from configuracoes import *


class Jogador(pygame.sprite.Sprite):
    """Classe responsável pelo jogador."""
    def __init__(self, pos, grupo):
        super().__init__(grupo)

        # Configurações gerais
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

        # Atributos de movimento
        self.direcao = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.velocidade = 200

    def entrada(self):
        """Função responsável por obter as entradas do jogador."""
        teclas = pygame.key.get_pressed()

        # Direção vertical
        if teclas[pygame.K_UP]:
            self.direcao.y = -1
        elif teclas[pygame.K_DOWN]:
            self.direcao.y = 1
        else:
            self.direcao.y = 0

        # Direção horizontal
        if teclas[pygame.K_LEFT]:
            self.direcao.x = -1
        elif teclas[pygame.K_RIGHT]:
            self.direcao.x = 1
        else:
            self.direcao.x = 0

    def movimento(self, delta):
        """Função responsável por mover o jogador."""
        # Normalizar o vetor
        if self.direcao.magnitude() > 0:
            self.direcao = self.direcao.normalize()

        # Movimento horizontal
        self.pos.x += self.direcao.x * self.velocidade * delta
        self.rect.centerx = self.pos.x

        # Movimento vertical
        self.pos.y += self.direcao.y * self.velocidade * delta
        self.rect.centery = self.pos.y

    def update(self, delta):
        """Função responsável por atualizar o jogador."""
        self.entrada()
        self.movimento(delta)
