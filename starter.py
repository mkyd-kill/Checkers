from abc import abstractclassmethod
import pygame
from board import Checkers
from constants import BLACK, GREEN, topleft_x, topleft_y, play_height, play_width, width, height

pygame.font.init()

class Starter:
    @abstractclassmethod
    def starter_text(surface, text, size, color):
        pass

    def welcome():
        run = True
        win = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        words = "Press any key to play!!!"
        while run:
            win.fill(BLACK)
            starter_text(win, words, 40, GREEN)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.init()
                    Checkers.Game()
                    run = False


def starter_text(surface, text, size, color):
    pygame.display.set_caption("Checkers")
    font = pygame.font.SysFont('Times New Roman', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (topleft_x + play_width / 2 - (label.get_width() / 2), topleft_y + play_height / 2 - (label.get_height() / 2)))