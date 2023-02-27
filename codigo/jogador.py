import os
import pygame
from suporte import *
from configuracoes import *
from temporizador import Temporizador


class Jogador(pygame.sprite.Sprite):
    """Classe responsável pelo jogador."""
    def __init__(self, pos, grupo):
        super().__init__(grupo)

        self.importar_graficos()
        self.estado = 'down_idle'
        self.indice_frame = 0

        # Configurações gerais
        self.image = self.animacoes[self.estado][self.indice_frame]
        self.rect = self.image.get_rect(center=pos)

        # Atributos de movimento
        self.direcao = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.velocidade = 200

        # Teporizadores
        self.temporizadores = {
            'ferramenta_uso': Temporizador(300, self.usar_ferramenta),
            'mudar_ferramenta': Temporizador(200),
            'semente_uso': Temporizador(300, self.usar_semente),
            'mudar_semente': Temporizador(200)
        }

        # Ferramentas
        self.ferramentas = ['hoe', 'axe', 'water']
        self.indice_ferramenta = 0
        self.ferramenta_selecionada = self.ferramentas[self.indice_ferramenta]

        # Sementes
        self.sementes = ['corn', 'tomato']
        self.indice_semente = 0
        self.semente_selecionada = self.sementes[self.indice_semente]

    def usar_ferramenta(self):
        pass

    def usar_semente(self):
        pass

    def importar_graficos(self):
        """Função responsável por importar os gráficos do jogador."""
        self.animacoes = {animacao: [] for animacao in os.listdir('../graficos/character')}

        for animacao in self.animacoes.keys():
            caminho_completo = f'../graficos/character/{animacao}'
            self.animacoes[animacao] = importar_pasta(caminho_completo)

    def animar(self, delta):
        """Função responsável por animar o jogador."""
        self.indice_frame += 4 * delta
        if self.indice_frame >= len(self.animacoes[self.estado]):
            self.indice_frame = 0
        self.image = self.animacoes[self.estado][int(self.indice_frame)]

    def entrada(self):
        """Função responsável por obter as entradas do jogador."""
        teclas = pygame.key.get_pressed()

        if not self.temporizadores['ferramenta_uso'].ativo:
            # Direção vertical
            if teclas[pygame.K_UP]:
                self.direcao.y = -1
                self.estado = 'up'
            elif teclas[pygame.K_DOWN]:
                self.direcao.y = 1
                self.estado = 'down'
            else:
                self.direcao.y = 0

            # Direção horizontal
            if teclas[pygame.K_LEFT]:
                self.direcao.x = -1
                self.estado = 'left'
            elif teclas[pygame.K_RIGHT]:
                self.direcao.x = 1
                self.estado = 'right'
            else:
                self.direcao.x = 0

            # Uso das ferramentas
            if teclas[pygame.K_x]:
                self.temporizadores['ferramenta_uso'].ativado()
                self.direcao = pygame.math.Vector2()
                self.indice_frame = 0

            # Mudar de ferramenta
            if teclas[pygame.K_z] and not self.temporizadores['mudar_ferramenta'].ativo:
                self.temporizadores['mudar_ferramenta'].ativado()
                self.indice_ferramenta += 1
                if self.indice_ferramenta == len(self.ferramentas):
                    self.indice_ferramenta = 0
                self.ferramenta_selecionada = self.ferramentas[self.indice_ferramenta]

            # Uso das sementes
            if teclas[pygame.K_a]:
                self.temporizadores['semente_uso'].ativado()
                self.direcao = pygame.math.Vector2()
                self.indice_frame = 0

            # Mudar de semente
            if teclas[pygame.K_s] and not self.temporizadores['mudar_semente'].ativo:
                self.temporizadores['mudar_semente'].ativado()
                self.indice_semente += 1
                if self.indice_semente == len(self.sementes):
                    self.indice_semente = 0
                self.semente_selecionada = self.sementes[self.indice_semente]

    def obter_estado(self):
        """Função responsável por obter o estado do jogador."""
        # Verificar se o jogador está parado
        if self.direcao.magnitude() == 0:
            self.estado = self.estado.split('_')[0] + '_idle'

        # Verificar qual ferramenta o jogador está usando
        if self.temporizadores['ferramenta_uso'].ativo:
            self.estado = self.estado.split('_')[0] + '_' + self.ferramenta_selecionada

    def atualizar_temporizadores(self):
        """Função responsável por ativar e desativar os temporizadores."""
        for temporizador in self.temporizadores.values():
            temporizador.update()

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
        self.obter_estado()
        self.atualizar_temporizadores()
        self.movimento(delta)
        self.animar(delta)
