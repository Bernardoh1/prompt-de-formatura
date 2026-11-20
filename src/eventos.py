"""Dados das situações de escolha do jogo (usadas em src/jogo.py)."""

# Cada situação é um dicionário:
#   texto   -> a situação mostrada ao jogador
#   opcoes  -> as três opções (0 = sem IA, 1 = IA e conferir, 2 = IA sem conferir)
#   ia_erra -> True se a IA erra nessa situação
#   x_rel   -> posição do ponto de escolha na tela (0.0 a 1.0 da largura)
ESCOLHAS = [
    {
        "texto": "Trabalho de cálculo para amanhã. O que fazer?",
        "opcoes": [
            "Resolver sozinho",
            "Usar a IA e conferir a resposta",
            "Copiar a resposta da IA",
        ],
        "ia_erra": True,
        "x_rel": 0.6,
    },
    {
        "texto": "Preciso de fontes para um seminário. E agora?",
        "opcoes": [
            "Pesquisar em livros e artigos",
            "Pedir fontes à IA e conferir cada uma",
            "Usar as fontes da IA sem conferir",
        ],
        "ia_erra": True,
        "x_rel": 0.8,
    },
    {
        "texto": "Resumo de um capítulo para a prova.",
        "opcoes": [
            "Ler e resumir com minhas palavras",
            "Pedir resumo à IA e comparar com o livro",
            "Decorar o resumo da IA",
        ],
        "ia_erra": False,
        "x_rel": 0.4,
    },
]