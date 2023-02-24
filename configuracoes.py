from pygame.math import Vector2

# Dimensões da tela
LARGURA = 1000
ALTURA = 650
TILE = 64

# Posicionamento do overlay
POSICAO_OVERLAY = {
    'ferramenta': (40, ALTURA - 15),
    'semente': (70, ALTURA - 5)
}

DESLOCAMENTO_FERRAMENTA_JOGADOR = {
    'esquerda': Vector2(-50, 40),
    'direita': Vector2(50, 40),
    'cima': Vector2(0, -10),
    'baixo': Vector2(0, 50)
}

# Continuar a partir de "LAYERS"