# 🐍 Snake Game — Python + Pygame

Um jogo clássico da cobrinha implementado em Python utilizando Pygame, com foco em modularização, arquitetura orientada a objetos, telas independentes, ranking persistente e personalização visual.

---

## 📌 Visão Geral
Este projeto implementa uma versão personalizada do clássico *Snake Game*, usando Pygame e princípios de POO.  
Inclui diversas telas, banco de dados com ranking, animações e tratamento de eventos.

---

## ✨ Funcionalidades
- Movimento fluido  
- Crescimento ao comer maçãs  
- Sistema de pontuação  
- Ranking em SQLite  
- Telas:
  - Start  
  - Menu  
  - Configurações  
  - Ranking  
  - Jogo  

---

## 🧱 Arquitetura
### 1. Entities
- Block  
- SnakeBlock  
- Snake  
- Apple  
- Player  

### 2. UI / Screens
- Start  
- Menu  
- Game  
- Ranking  
- Configs  

### 3. Banco de Dados
- Classe Database (SQLite)

---

## 📂 Estrutura de Pastas
```
project/
│── ui/
│── entities/
│── utils/
│── assets/
│── main.py
│── README.md
```

---

## 🚀 Como Executar
```
pip install -r requirements.txt
python main.py
```

---

## 👥 Autores
- Fábio Braga Giugni  
- Samuel Felipe Verçosa Gonçalves  
- Thales Eduardo Dias de Souza  
