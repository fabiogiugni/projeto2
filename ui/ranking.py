import pygame
from utils.settings import WHITE, LIGHT_GREEN, BLACK, GOLDEN, SILVER, BROWN
from ui.screen import Screen
from ui.scoreBoard import ScoreBoard

class Ranking(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.__scores = []

    def handle_events(self, event):
        pass
    
    def update(self):
        self.update_blinker()

    def hover(self):
        pass

    def addScore(self, name : str, score : ScoreBoard):
        for sb in self.__scores:
            if sb[0] == name:
                return
        i = 0
        for sb in self.__scores:
            s = sb[1]
            if s.score < score.score:
                break
            else:
                i += 1

        self.__scores.insert(i, [name, score, 310 + (32*i)])
        for i in range(len(self.__scores)):
            self.__scores[i][2] = 310 + (36*i)

    def draw(self, display):
        super().draw(display) 

        ## ADICIONANDO JOGADORES TESTES MANUALMENTE
        score1 = ScoreBoard(None)
        for i in range(9):
            score1.increase_apple()
        for i in range(25):
            score1.update_time()
        score1.update_score()
        
        score2 = ScoreBoard(None)
        for i in range(7):
            score2.increase_apple()
        for i in range(23):
            score2.update_time()

        score3 = ScoreBoard(None)
        for i in range(8):
            score3.increase_apple()
        for i in range(22):
            score3.update_time()

        score4 = ScoreBoard(None)
        for i in range(2):
            score4.increase_apple()
        for i in range(32):
            score4.update_time()

        self.addScore("Thales", score1)
        self.addScore("Fábio", score2)
        self.addScore("Samuel", score3)
        self.addScore("Teste", score4)
        ###############################

        # Título principal
        title = self.title_font.render("SNAKE GAME", False, WHITE)
        display.blit(
            title,
            (self.game.size[0]//2 - title.get_width()//2, 100)
        )

        # Subtítulo "Ranking" com efeito de piscar
        if (not self.should_blink):
            press = self.text_font.render("Ranking", False, WHITE)
            display.blit(
                press,
                (self.game.size[0]//2 - press.get_width()//2, 220)
            )
        else:
            press = self.text_font.render("Ranking", False, LIGHT_GREEN)
            display.blit(
                press,
                (self.game.size[0]//2 - press.get_width()//2, 220)
            )

        # Cabeçalho da tabela
        header = self.text_font.render("Name         Apples      Time      Score", False, WHITE)
        display.blit(
            header,
            (self.game.size[0]//2 - header.get_width()//2, 280)
        )

        # Linha separadora abaixo do cabeçalho
        separator_y = 310
        pygame.draw.line(display, WHITE, 
                        (self.game.size[0]//2 - header.get_width()//2, separator_y),
                        (self.game.size[0]//2 + header.get_width()//2, separator_y), 2)

        # Posição inicial para os scores
        start_y = 330
        line_height = 40
        
        # Ordenar scores por pontuação (maior primeiro)
        sorted_scores = sorted(self.__scores, key=lambda x: x[1].score, reverse=True)
        
        # Desenhar cada linha do placar
        for i, sb in enumerate(sorted_scores):
            name, score_obj, _ = sb
            
            # Cor alternada para as linhas (opcional)
            row_color = WHITE
            # Alternar cores para melhor legibilidade:
            # row_color = LIGHT_GRAY if i % 2 == 0 else WHITE
            
            # Formatar os dados com espaçamento consistente
            name_text = f"{name:<12}"      # 12 caracteres para nome
            apples_text = f"{score_obj.apples:>2}"        # 2 dígitos para maçãs
            time_text = f"{score_obj.time:>4}"           # 4 dígitos para tempo
            score_text = f"{score_obj.score:>5}"         # 5 dígitos para score
            
            # Texto completo da linha
            line_text = f"{name_text}    {apples_text}        {time_text}       {score_text}"
            
            text = self.text_font.render(line_text, False, row_color)
            
            # Posicionar a linha
            y_pos = start_y + (i * line_height)
            
            # Destacar o primeiro colocado (opcional)
            if i == 0:
                # Desenhar um fundo destacado para o primeiro lugar
                highlight_rect = pygame.Rect(
                    self.game.size[0]//2 - text.get_width()//2 - 10,
                    y_pos - 5,
                    text.get_width() + 20,
                    text.get_height() + 10
                )
                pygame.draw.rect(display, LIGHT_GREEN, highlight_rect, border_radius=5)
                pygame.draw.rect(display, WHITE, highlight_rect, 2, border_radius=5)
                text = self.text_font.render(line_text, False, BLACK)  # Texto preto no fundo verde
            
            display.blit(
                text,
                (self.game.size[0]//2 - text.get_width()//2, y_pos)
            )
            
            # Adicionar medalha para os primeiros lugares (opcional)
            if i < 3:  # Primeiro, segundo e terceiro lugar
                medal_colors = [GOLDEN, SILVER, BROWN]  # Ouro, Prata, Bronze
                medal_radius = 10
                medal_x = self.game.size[0]//2 - header.get_width()//2 - 20
                medal_y = y_pos + text.get_height()//2
                
                pygame.draw.circle(display, medal_colors[i], (medal_x, medal_y), medal_radius)
                
                # Número da posição dentro da medalha
                medal_text = self.text_font.render(str(i+1), False, BLACK)
                display.blit(medal_text, (medal_x - medal_text.get_width()//2, medal_y - medal_text.get_height()//2))
