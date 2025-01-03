import pygame
from utils import recortar_imagem


class Button:
    def __init__(self, left, top, w, h, imagem):
        self.rect = pygame.Rect(left, top, w, h)
        self.imagem = imagem
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Verifica se o mouse está sobre o botão
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Desenha o botão na tela usando a imagem
        surface.blit(self.imagem, (self.rect.x, self.rect.y))

        return action


class StartButton(Button):
    def __init__(self, left, top, w, h, imagem_original):
        start_imagem = recortar_imagem(158, 54, 300, 100, imagem_original)  # Ajuste as coordenadas conforme necessário
        Button.__init__(self, left, top, w, h, start_imagem)


class PauseButton(Button):
    def __init__(self, left, top, w, h, imagem_original):
        pausa_imagem = recortar_imagem(158, 13, 300, 60, imagem_original)  # Ajuste as coordenadas conforme necessário
        Button.__init__(self, left, top, w, h, pausa_imagem)


class DeathButton(Button):
    def __init__(self, left, top, w, h, imagem_original):
        death_imagem = recortar_imagem(486, 107, 530, 160, imagem_original)  # Ajuste as coordenadas conforme necessário
        Button.__init__(self, left, top, w, h, death_imagem)


class ScoreButton(Button):
    def __init__(self, left, top, w, h, imagem_original):
        score_imagem = recortar_imagem(480, 20, 620, 50, imagem_original)  # Ajuste as coordenadas conforme necessário
        Button.__init__(self, left, top, w, h, score_imagem)


class ResumeButton(Button):
    def __init__(self, left, top, w, h, imagem_original):
        resume_imagem = recortar_imagem(158, 13, 300, 60, imagem_original)  # Ajuste as coordenadas conforme necessário
        Button.__init__(self, left, top, w, h, resume_imagem)


class MenuButton(Button):
    def __init__(self, left, top, w, h, imagem_original):
        menu_imagem = recortar_imagem(300, 13, 460, 50, imagem_original)  # Ajuste as coordenadas para o botão Menu
        Button.__init__(self, left, top, w, h, menu_imagem)
