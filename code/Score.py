import sys
from datetime import datetime

import pygame
from pygame import Surface, Font, Rect, KEYDOWN
from pygame.constants import K_RETURN, K_BACKSPACE, K_ESCAPE

from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE, C_CYAN
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        text = 'Enter Player 1 name (4 characters):'
        score = player_score[0]
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'], 1)
            if game_mode == MENU_OPTION[0]:
                text = 'Enter Player name (4 characters):'
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) // 2
                text = 'Enter Team name (4 characters):'
            if game_mode == MENU_OPTION[2]:
                if player_score[1] >= player_score[0]:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'

            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'], 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'], 1)
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'], 1)
        self.score_text(20, ' NAME     SCORE        DATE      ', C_CYAN, SCORE_POS['Label'], 1)
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', C_WHITE,
                            SCORE_POS[list_score.index(player_score)], 1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_weight: int):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans", size=text_size)

        # 1. Renderiza o texto base
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # 2. Cria uma cópia idêntica para o efeito de "falso negrito"
        shadow_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # Desloca apenas 1 píxel para a direita
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + font_weight, text_center_pos[1]))

        # 3. Desenha ambos na tela (o deslocamento cria o peso intermediário)
        self.window.blit(source=shadow_surf, dest=shadow_rect)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_date}"