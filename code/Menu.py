#!/usr/bin/pithon
# -*- coding: utf-8 -*-
import pygame
from pygame import Font, Surface, Rect
g
from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Mountain', COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLOR_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text2(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), (200 + 25 * i)))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # 1. Renderiza o texto base
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # 2. Cria uma cópia idêntica para o efeito de "falso negrito"
        shadow_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # Desloca apenas 1 pixel para a direita
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + 2, text_center_pos[1]))

        # 3. Desenha ambos na tela (o deslocamento cria o peso intermediário)
        self.window.blit(source=shadow_surf, dest=shadow_rect)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_text2(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # 1. Renderiza o texto base
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # 2. Cria uma cópia idêntica para o efeito de "falso negrito"
        shadow_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # Desloca apenas 1 pixel para a direita
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + 1, text_center_pos[1]))

        # 3. Desenha ambos na tela (o deslocamento cria o peso intermediário)
        self.window.blit(source=shadow_surf, dest=shadow_rect)
        self.window.blit(source=text_surf, dest=text_rect)
