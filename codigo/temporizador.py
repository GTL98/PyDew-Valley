import pygame


class Temporizador:
    def __init__(self, duracao, func=None):
        self.duracao = duracao
        self.func = func
        self.tempo_comeco = 0
        self.ativo = False

    def ativado(self):
        """Função responsável por ativar o temporizador."""
        self.ativo = True
        self.tempo_comeco = pygame.time.get_ticks()

    def desativado(self):
        """Função responsável por desativar o temporizador."""
        self.ativo = False
        self.tempo_comeco = 0

    def update(self):
        """Função responsável por atualizar o temporizador."""
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_comeco >= self.duracao:
            self.desativado()
            if self.func:
                self.func()