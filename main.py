
import pygame
import random

pygame.init()

# Janela
LARGURA = 400
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
AZUL = (100, 149, 237)
VERDE = (34, 177, 76)

# Jogador
x_passaro = 60
y_passaro = ALTURA//2
velocidade = 0
gravidade = 0.5
pulo = -8
raio = 20

# Cano
cano_largura = 70
cano_vel = 3
distancia = 150
cano_x = LARGURA
cano_altura = random.randint(50, 450)

# Pontuação
pontos = 0
fonte = pygame.font.SysFont("arial", 30)

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocidade = pulo

    # Física do pássaro
    velocidade += gravidade
    y_passaro += velocidade

    # Movimento dos canos
    cano_x -= cano_vel
    if cano_x < -cano_largura:
        cano_x = LARGURA
        cano_altura = random.randint(50, 450)
        pontos += 1

    # Colisões (paredes)
    if y_passaro - raio <= 0 or y_passaro + raio >= ALTURA:
        rodando = False

    # Colisão com canos
    if (x_passaro + raio > cano_x and x_passaro - raio < cano_x + cano_largura):
        if y_passaro - raio < cano_altura or y_passaro + raio > cano_altura + distancia:
            rodando = False

    # Desenho
    tela.fill(AZUL)

    # Pássaro
    pygame.draw.circle(tela, BRANCO, (x_passaro, int(y_passaro)), raio)

    # Canos
    pygame.draw.rect(tela, VERDE, (cano_x, 0, cano_largura, cano_altura))
    pygame.draw.rect(tela, VERDE, (cano_x, cano_altura + distancia, cano_largura, ALTURA))

    # Pontos
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
print("GAME OVER - Pontuação final:", pontos)
