# This is the game board initialisation, variables usage
from game import MainGame
import pygame
from constants import SQUARE_SIZE, WHITE, WIDTH, HEIGHT
from abc import abstractclassmethod
from minimax.algorithm import minimax

pygame.init()
 
class Checkers():
    @abstractclassmethod
    def get_row_col_from_mouse(pos):
        pass

    def Game():
        pygame.init()
        WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Python Checkers")
        FPS = 60
        run = True
        game = MainGame(WIN)
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(FPS)

            # initializing the ai game move
            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), 4, WHITE, game)
                game.ai_move(new_board)

            if game.winner() != None:
                print(game.winner())
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

            game.update()


def get_row_col_from_mouse(pos):
    ''' This gets user and computer mouse input moves '''
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    print("Row: {}, Col: {}".format(row, col))
    return row, col