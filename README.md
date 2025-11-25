🐍 Snake Game — Python + Pygame

Um jogo clássico da cobrinha implementado em Python utilizando Pygame, com foco em modularização, arquitetura orientada a objetos, telas independentes, ranking persistente em banco de dados e personalização visual.

📌 Sumário

Visão Geral

Funcionalidades

Arquitetura

Estrutura de Pastas

Tecnologias Utilizadas

Como Executar

Detalhes de Implementação

Capturas / GIFs (opcional)

Autores

🎮 Visão Geral

Este projeto implementa uma versão personalizada do clássico Snake Game, utilizando Pygame e princípios de Programação Orientada a Objetos (POO).
O jogo inclui diversas telas, sistema de pontuação, ranking persistente em SQLite, animações, tratamento de eventos, além de modularização clara entre entidades, interface e gerenciamento de estados.

✨ Funcionalidades

✔️ Movimento fluido da cobrinha
✔️ Crescimento ao comer maçãs
✔️ Sistema de pontuação baseado em tempo e maçãs
✔️ Detecção de colisões (corpo e bordas)
✔️ Ranking salvo em banco de dados SQLite
✔️ Interface modular com múltiplas telas:

Tela inicial

Menu

Configurações

Ranking

Jogo em execução

✔️ Animações de piscar texto
✔️ Bordas vermelhas quando o jogador morre
✔️ Suporte a imagens e rotação da cabeça da cobra

🧱 Arquitetura

O projeto segue uma estrutura modular inspirada em um padrão MVC simplificado:

1. Entities (Entidades do jogo)

Block: bloco gráfico base

SnakeBlock: segmento da cobra + direção + movimento

Snake: gerencia corpo, colisões, crescimento e morte

Apple: maçã com reposicionamento aleatório

2. UI / Screens (Telas do jogo)

Cada tela herda de Screen e implementa ScreenInterface:

Start: tela inicial

Menu: seleção de opções

Configs: futuras configurações

Ranking: exibição do ranking

Game: lógica da partida

3. Lógica de Jogo

Atualização do estado

Detecta eventos (teclado/mouse)

Controla FPS

Renderiza sprites e textos

4. Banco de Dados

Gerenciado via classe Database, utilizada por Player:

Armazena: nome, maçãs, tempo e score

Usado para construir ranking

📂 Estrutura de Pastas
project/
│── ui/
│   ├── screenInterface.py
│   ├── screen.py
│   ├── start.py
│   ├── menu.py
│   ├── game.py
│   ├── ranking.py
│   └── configs.py
│
│── entities/
│   ├── block.py
│   ├── apple.py
│   ├── snakeBlock.py
│   ├── snake.py
│   └── player.py
│
│── utils/
│   ├── settings.py
│   └── database.py
│
│── assets/
│   ├── background.jpg
│   ├── snake_head.png
│   ├── snake_body.png
│   └── fontes, imagens, etc.
│
│── main.py  (ou start.py / app.py)
│── README.md
└── requirements.txt

🛠️ Tecnologias Utilizadas

Python 3.10+

Pygame

SQLite3

Paradigma Orientado a Objetos

Arquitetura modular com telas (screen manager)

🚀 Como Executar
1. Clone o repositório
git clone https://github.com/SEU_USUARIO/snake-game.git
cd snake-game

2. Crie e ative um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate   # Linux
venv\Scripts\activate      # Windows

3. Instale as dependências
pip install -r requirements.txt

4. Execute o jogo
python main.py

🧩 Detalhes de Implementação
🟦 Movimentação da Cobra

A cobra é formada por objetos SnakeBlock.
Cada bloco herda de Block e possui método walk() que move o bloco na direção atual.

Crescimento ocorre via:

def grow(self):
    new_block = SnakeBlock(...)
    self.__blocks.append(new_block)

🍎 Maçã

A maçã tem posição gerada aleatoriamente em múltiplos de SNAKE_SPEED:

self._position = (
    randint(0, max_x) * SNAKE_SPEED,
    randint(0, max_y) * SNAKE_SPEED
)

💥 Detecção de Colisão

Simples comparação de posições entre a cabeça e:

Bordas

Demais segmentos

Maçã

🧮 Pontuação

Implementada em ScoreBoard:

apples: número de frutas comidas

time: tempo total

score: função calculada sobre ambos

🖼️ Renderização

Superfícies semi-transparentes

Rotação da cabeça da cobra

Atualização de FPS com clock.tick()

📸 Capturas / GIFs (opcional)

Se quiser, posso gerar uma sessão assim:

![Menu](assets/screens/menu.png)
![Gameplay](assets/screens/gameplay.gif)
![Game Over](assets/screens/gameover.png)

👥 Autores

Fábio Braga Giugni

Samuel Felipe Verçosa Gonçalves

Thales Eduardo Dias de Souza# projeto2
