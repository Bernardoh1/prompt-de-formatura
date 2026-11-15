# Proposta Inicial do Jogo
 
## 1. Nome provisório do jogo
 
**Nome:** Prompt de Formatura
 
## 2. Integrantes do grupo
 
* Nome 1: Bernardo Henrique (GitHub: Bernardoh1)
Projeto desenvolvido individualmente.
 
## 3. Tema escolhido
 
**Tema:** Uso de IA generativa (chatbots) na vida universitária: apoio aos estudos e riscos de confiar nas respostas sem conferir. Aspectos de responsabilidade trabalhados: confiabilidade, análise crítica dos resultados e integridade acadêmica.
 
**Como esse tema se relaciona com o jogo?**
Em cada ponto de escolha da faculdade, o jogador decide se usa a IA e como usa. Algumas respostas da IA estão erradas e o jogador não é avisado. Quem confia cegamente acumula um valor escondido de dependência da IA, e esse valor muda a pontuação, o caminho e o final da personagem. O tema muda as decisões e o desfecho da partida, e não só o cenário.
 
## 4. Tipo de jogo
 
**Tipo escolhido:** Jogo 2D lateral simples, com movimento, pulo e escolhas, inspirado no jogo mobile "A Vida é um Jogo", mas passado só na fase da faculdade.
 
## 5. Descrição geral do jogo
 
**Descrição:**
A tela mostra uma cena da faculdade (sala de aula, biblioteca, laboratório ou estágio), com os indicadores da personagem. O jogador controla a estudante, que anda para os lados e pula. Pelo cenário há livros para coletar e pontos de escolha. Ao chegar a um ponto de escolha, o jogo mostra uma situação e três opções: não usar IA, usar a IA e conferir, ou copiar a resposta sem conferir. O desafio é perceber quando a IA pode estar errada. A IA do jogo é simulada com condicionais, listas e dicionários.
 
## 6. Objetivo do jogador
 
**Objetivo:**
Levar a personagem até o fim da última cena (a formatura) com o melhor desempenho possível, equilibrando nota e aprendizado de verdade, e evitando a dependência da IA.
 
## 7. Regras principais
 
* Regra 1: A estudante anda e pula pelas cenas, coletando livros que dão conhecimento e pontos.
* Regra 2: Nos pontos de escolha, o jogador escolhe uma das três opções (sem IA, IA com conferência ou IA sem conferência).
* Regra 3: Cada escolha altera nota, conhecimento e dependência da IA.
* Regra 4: Em alguns pontos a IA erra, e quem não conferiu perde nota.
* Regra 5: No fim da última cena, a dependência acumulada define o desfecho.
## 8. Condição de vitória
 
**Condição de vitória:**
Chegar à formatura com boa nota e baixa dependência da IA (final bom). Há também um final intermediário, em que a personagem forma, mas tem dificuldades no estágio ou no TCC.
 
## 9. Condição de derrota ou encerramento
 
**Condição de derrota ou encerramento:**
A nota chegar a zero durante o jogo (reprovação), ou terminar a última cena com dependência alta da IA (final ruim, por plágio e falta de preparo).
 
## 10. Elementos previstos no jogo
 
* Personagem ou elemento principal: a estudante, que anda e pula pelo cenário.
* Obstáculos ou desafios: pontos de escolha com respostas erradas da IA e plataformas simples.
* Itens ou objetos de interação (se houver): livros coletáveis e pontos de escolha.
* Pontuação, vidas, tempo ou progresso: nota, conhecimento, pontuação e cena atual, com recorde salvo em arquivo. A dependência da IA fica escondida e só aparece no final.
## 11. Controles previstos
 
**Controles:**
Setas para andar, espaço para pular, ENTER para interagir com um ponto de escolha, teclas 1, 2 e 3 para escolher e ESC para sair.
 
## 12. Principais dificuldades esperadas
 
* Dificuldade 1: Primeiro projeto com Pygame (loop principal, movimento e pulo).
* Dificuldade 2: Trocar de cena e organizar o estado do jogo, separando a lógica da interface.
* Dificuldade 3: Escrever os testes das funções de lógica e equilibrar escolhas e finais.
## 13. Escopo mínimo para a entrega final
 
**Escopo mínimo:**
Quatro cenas, de 6 a 8 pontos de escolha, 3 finais diferentes, movimento e pulo da personagem, livros coletáveis, indicadores na tela, recorde salvo em arquivo e testes das funções principais de lógica. Gráficos simples, feitos com formas geométricas.
 
## 14. Possíveis melhorias, caso haja tempo
 
* Melhoria 1: Sprites e cenários desenhados.
* Melhoria 2: Sons e animações simples.
* Melhoria 3: Mais cenas e eventos sorteados a cada partida.
## 15. Organização inicial do código, estruturas de dados, arquivos e testes
 
**Organização do código**
 
* `main.py`: ponto de entrada.
* `src/jogo.py`: loop do jogo, desenho das cenas e movimento da personagem.
* `src/config.py`: constantes (tela, cores, FPS, velocidade e força do pulo).
* `src/funcoes.py`: funções de regras (aplicar escolha, calcular final, calcular pontuação).
* `src/eventos.py`: dados das cenas e dos pontos de escolha.
* `src/dados.py`: leitura e gravação do recorde.
* `tests/`: testes com `pytest` para as funções de lógica.
**Estruturas de dados previstas**
 
* Lista de dicionários para os pontos de escolha (situação, opções, efeito de cada opção e se a IA erra).
* Dicionário para o estado da partida (nota, conhecimento, dependência, pontuação e cena atual).
* Lista de cenas e lista de livros coletáveis.
* Tuplas para posições e cores.
**Uso de arquivos**
 
* Arquivo em `data/` para guardar o recorde de pontuação, lido ao abrir o jogo e atualizado ao final da partida.
**Testes planejados**
 
* Testes com `pytest` para as funções de lógica, sem depender da janela do Pygame: aplicar uma escolha (nota, conhecimento e dependência mudam como esperado), calcular o final a partir da dependência e da nota, calcular a pontuação e ler/gravar o recorde.
## 16. Recursos
 
Python, Pygame, pytest e o template da disciplina. Imagens, fontes ou sons externos, se forem usados, serão listados no README.md com origem e licença.
 
## 17. Declaração de originalidade
 
Declaro que esta proposta é original e foi elaborada por mim para esta disciplina. A ideia é inspirada no jogo mobile "A Vida é um Jogo", mas a ambientação na faculdade, as regras, as escolhas e a mecânica de uso da IA são autorais.
 
