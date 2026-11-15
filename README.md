# Prompt de Formatura

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.
Tema: **Inteligência Artificial no Cotidiano: Aplicações e Uso Responsável**.

## Integrantes do grupo

* Bernardo Henrique (GitHub: Bernardoh1)

## Estrutura do projeto

* `main.py`: ponto de entrada da aplicação.
* `src/`: código-fonte principal do jogo (loop, regras, cenas e dados).
* `assets/`: imagens, fontes e sons.
* `data/`: arquivos persistentes (recorde/ranking).
* `tests/`: testes unitários com `pytest`.
* `docs/`: documentação do projeto, incluindo a proposta inicial.

## Descrição do jogo

Jogo 2D lateral inspirado no jogo mobile "A Vida é um Jogo", mas passado só na fase da faculdade. O jogador controla uma estudante que anda e pula por cenas como sala de aula, biblioteca, laboratório e estágio. Pelo cenário há livros para coletar e pontos de escolha ("CHOICE"). Em cada ponto de escolha, o jogador decide como agir:

1. Não usar IA;
2. Usar a IA para estudar e conferir a resposta;
3. Copiar a resposta da IA sem conferir.

Algumas respostas da IA parecem corretas, mas estão erradas, inventadas ou copiadas, e o jogador não é avisado. Quem confia cegamente ganha nota rápido, mas aumenta um indicador escondido de dependência. No final, esse indicador define qual caminho a personagem segue.

## Objetivo do jogador

Chegar à formatura com o melhor desempenho possível, equilibrando nota e aprendizado de verdade. O jogador precisa decidir quando confiar na IA e quando conferir o que ela respondeu.

## Regras do jogo

* A estudante anda e pula pelas cenas, coletando livros que aumentam o conhecimento e a pontuação.
* Nos pontos de escolha, o jogador escolhe entre não usar IA, usar e conferir, ou copiar sem conferir.
* Cada escolha altera a nota, o conhecimento e a dependência da IA.
* Quando a IA erra e o jogador não conferiu, ele sofre uma penalidade na nota.
* Ao final da última cena, a dependência acumulada define o desfecho: formatura tranquila, dificuldades no estágio/TCC ou reprovação por plágio e falta de preparo. Se a nota chegar a zero, a partida termina antes.
* O desempenho final (pontuação) pode ser salvo como recorde em `data/`.

## Controles

* Seta para a esquerda e para a direita: andar
* Espaço: pular
* ENTER: interagir com um ponto de escolha
* Teclas 1, 2 e 3: escolher uma das opções
* ESC: sair do jogo

## Uso responsável de IA no jogo (integração com o tema)

O jogo trabalha confiabilidade e análise crítica: a IA nem sempre acerta, e conferir as informações muda o resultado da partida. A IA do jogo é simulada com condicionais, listas e dicionários, sem uso de modelos reais.

## Como executar o projeto

1. Clonar o repositório

```
git clone https://github.com/Bernardoh1/prompt-de-formatura.git
cd prompt-de-formatura
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```
python -m pytest
```

## Recursos externos utilizados

* (listar aqui imagens, sons, fontes, código ou tutoriais usados, com origem e licença quando possível)

## Decisões técnicas

* (registrar aqui, ao longo do desenvolvimento, as principais decisões do projeto)

## Checklist mínimo para entrega

* [ ] Preencher este README com nome final, descrição real, regras e controles do jogo.
* [ ] Atualizar `docs/proposta.MD` com a proposta.
* [ ] Garantir que o jogo executa com `python main.py`.
* [ ] Garantir que os testes passam com `pytest`.
