import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    limitar_valor,
    verificar_colisao,
    aplicar_escolha,
    calcular_final,
)
from src.eventos import ESCOLHAS
from src.sprites import pegar_sprite

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Teclas 1, 2 e 3 -> número da opção (0, 1 ou 2)
TECLAS_OPCOES = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2}


def desenhar_texto(tela, fonte, texto, x, y, cor=BRANCO):
    """Escreve um texto na tela, com o canto superior esquerdo em (x, y)."""
    tela.blit(fonte.render(texto, True, cor), (x, y))


def executar_jogo():
    """Executa o loop principal do jogo e controla estado e escolhas."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 28)
    rodando = True

    # Imagens recortadas do spritesheet (as mesmas do template)
    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)
    gem_image = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)

    # Os dois ficam "no chão" (mesmo y); a gema é o ponto de escolha
    chao_y = ALTURA_TELA - 200

    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(100, chao_y)),
    }
    gema = {
        "imagem": gem_image,
        "rect": gem_image.get_rect(topleft=(int(LARGURA_TELA * ESCOLHAS[0]["x_rel"]), chao_y)),
    }

    velocidade = 5

    # Estado da partida: a dependência da IA fica escondida até o final
    estado = {"nota": 70, "conhecimento": 0, "dependencia": 0}
    indice = 0            # qual situação de escolha é a atual
    em_escolha = False    # True enquanto o painel de opções está aberto
    mensagem = ""         # resultado da última escolha

    while rodando:
        relogio.tick(FPS)
        fim = indice >= len(ESCOLHAS)
        perto = verificar_colisao(jogador["rect"], gema["rect"])

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                elif em_escolha and evento.key in TECLAS_OPCOES:
                    escolha = ESCOLHAS[indice]
                    mensagem = aplicar_escolha(
                        estado, TECLAS_OPCOES[evento.key], escolha["ia_erra"]
                    )
                    em_escolha = False
                    indice += 1
                    if indice < len(ESCOLHAS):
                        gema["rect"].x = int(LARGURA_TELA * ESCOLHAS[indice]["x_rel"])

                elif evento.key == pygame.K_RETURN and perto and not fim:
                    em_escolha = True

        # Movimento nas 4 direções (apertando duas teclas, anda na diagonal),
        # e só quando o painel está fechado
        teclas = pygame.key.get_pressed()
        if not em_escolha and not fim:
            if teclas[pygame.K_LEFT]:
                jogador["rect"].x -= velocidade
            if teclas[pygame.K_RIGHT]:
                jogador["rect"].x += velocidade
            if teclas[pygame.K_UP]:
                jogador["rect"].y -= velocidade
            if teclas[pygame.K_DOWN]:
                jogador["rect"].y += velocidade

        # Mantém o jogador dentro da tela
        jogador["rect"].x = limitar_valor(
            jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width
        )
        jogador["rect"].y = limitar_valor(
            jogador["rect"].y, 0, ALTURA_TELA - jogador["rect"].height
        )

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Nota: {estado['nota']} | Conhecimento: {estado['conhecimento']}"
        )

        # ---------- Desenho ----------
        tela.fill(CINZA)

        if not fim:
            tela.blit(gema["imagem"], gema["rect"])
            if perto and not em_escolha:
                desenhar_texto(
                    tela, fonte, "ENTER para decidir",
                    gema["rect"].x - 40, gema["rect"].y - 30, PRETO,
                )
        tela.blit(jogador["imagem"], jogador["rect"])

        desenhar_texto(
            tela, fonte,
            f"Nota: {estado['nota']}   Conhecimento: {estado['conhecimento']}",
            20, 15, PRETO,
        )
        if mensagem and not em_escolha:
            desenhar_texto(tela, fonte, mensagem, 20, 50, PRETO)

        if em_escolha:
            escolha = ESCOLHAS[indice]
            pygame.draw.rect(tela, PRETO, (40, 90, LARGURA_TELA - 80, 220))
            desenhar_texto(tela, fonte, escolha["texto"], 60, 110)
            for i, opcao in enumerate(escolha["opcoes"]):
                desenhar_texto(tela, fonte, f"{i + 1} - {opcao}", 60, 160 + i * 40)

        if fim:
            pygame.draw.rect(tela, PRETO, (40, 90, LARGURA_TELA - 80, 220))
            desenhar_texto(tela, fonte, "Fim da demonstração", 60, 110)
            desenhar_texto(tela, fonte, f"Dependência da IA: {estado['dependencia']}", 60, 160)
            desenhar_texto(tela, fonte, calcular_final(estado), 60, 200)
            desenhar_texto(tela, fonte, "ESC para sair", 60, 260)

        pygame.display.flip()

    pygame.quit()