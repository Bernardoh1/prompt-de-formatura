def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)

def aplicar_escolha(estado, opcao, ia_erra):
    """Aplica o efeito de uma escolha sobre o estado da partida.

    Args:
        estado (dict): dicionário com "nota", "conhecimento" e "dependencia".
        opcao (int): 0 = sem IA, 1 = IA e conferir, 2 = IA sem conferir.
        ia_erra (bool): True se a IA errou nessa situação.

    Returns:
        str: mensagem explicando o que aconteceu.
    """
    if opcao == 0:
        estado["nota"] += 5
        estado["conhecimento"] += 3
        mensagem = "Você resolveu sozinho. Demorou, mas aprendeu."
    elif opcao == 1:
        estado["nota"] += 8
        estado["conhecimento"] += 3
        if ia_erra:
            mensagem = "A IA errou, mas você conferiu e corrigiu!"
        else:
            mensagem = "Você usou a IA e conferiu a resposta. Boa!"
    else:
        estado["dependencia"] += 2
        if ia_erra:
            estado["nota"] -= 10
            mensagem = "A IA errou e você copiou sem conferir!"
        else:
            estado["nota"] += 10
            mensagem = "A IA acertou, mas você nem conferiu."

    estado["nota"] = limitar_valor(estado["nota"], 0, 100)
    return mensagem


def calcular_final(estado):
    """Define o final da partida a partir da nota e da dependência da IA.

    Args:
        estado (dict): dicionário com "nota", "conhecimento" e "dependencia".

    Returns:
        str: texto do final alcançado.
    """
    if estado["dependencia"] >= 4 or estado["nota"] < 50:
        return "Final ruim: dependência demais da IA."
    if estado["dependencia"] >= 2:
        return "Final intermediário: formou, mas com dificuldades."
    return "Final bom: formou com aprendizado de verdade!"