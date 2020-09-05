from game import Game, GamePlayingAgent, GameSolvingAgent, Algorithm
from tictactoe import TicTacToe
from openfield_tictactoe import OpenFieldTicTacToe
import pygame as _


class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


def get_img(icon: str):
    return _.image.load('sprites/{}.png'.format(icon.lower()))


def get_game_end_img(game: Game):
    if game.winner(game.state) == "TIE":
        return _.image.load("sprites/tie.png")
    else:
        return _.image.load("sprites/win_{}.png".format(str(game.winner(game.state)).lower()))


class GameRunner:
    def __init__(self, game: Game, algo: Algorithm = Algorithm.MinMax, user_plays_first=True, **kwargs):
        self.game = game
        self.algo = algo
        self.agent = GamePlayingAgent(game=game, algo=algo, **kwargs)
        self.icon_size = 50
        self.line_size = 5
        self.user_plays_first = user_plays_first

    @property
    def size(self):
        return len(self.game.initial_state)

    @property
    def board_size(self):
        return [self.size * (self.icon_size + self.line_size) + self.line_size] * 2

    def start(self):
        if not self.user_plays_first:
            self.agent.play()
        _.init()
        screen: _.Surface = _.display.set_mode(self.board_size)
        bg_color = (255, 255, 255)
        font = _.font.SysFont(_.font.get_default_font(), 24)
        running = True
        while running:
            events = _.event.get()
            
            # Manage Events
            for event in events:
                if event.type == _.QUIT:
                    running = False

                if event.type == _.MOUSEBUTTONUP:
                    if self.agent.game_ended:
                        running = False
                    else:
                        self.listen_input(_.mouse.get_pos())
                        
            # Background Color
            screen.fill(bg_color)
            
            # Draw Lines
            self.draw_background(screen)
            # Draw Game State
            self.draw_icons(screen, alpha=(128 if self.agent.game_ended else 255))

            # Show Result if game ends
            if self.agent.game_ended:
                img = _.transform.scale(get_game_end_img(self.game), self.board_size)
                square = img.get_rect()
                square.move((0, 0))
                screen.blit(img, square)

            _.display.flip()

        _.quit()

    def listen_input(self, pos):
        for i in range(self.size):
            for j in range(self.size):
                square = _.rect.Rect(j * (self.icon_size + self.line_size) + self.line_size,
                                     i * (self.icon_size + self.line_size) + self.line_size,
                                     self.icon_size, self.icon_size)
                if square.collidepoint(*pos):
                    if self.game.state[i][j] == ' ':
                        # If making user move fails (redundant check)
                        if self.agent.user_move((i + 1, j + 1)):
                            self.agent.play()

    def draw_background(self, screen: _.Surface):
        # Horizontal Lines
        for i in range(self.size + 1):
            line = _.rect.Rect(0, i * (self.icon_size + self.line_size), self.board_size[0], self.line_size)
            _.draw.rect(screen, Color.BLACK, line)
        for i in range(self.size + 1):
            line = _.rect.Rect(i * (self.icon_size + self.line_size), 0, self.line_size, self.board_size[0])
            _.draw.rect(screen, Color.BLACK, line)

    def draw_icons(self, screen: _.Surface, alpha=255):
        for i in range(self.size):
            for j in range(self.size):
                icon = self.game.state[i][j]
                if icon == ' ':
                    continue
                img = _.transform.scale(get_img(icon), (self.icon_size, self.icon_size))
                square = img.get_rect()
                square = square.move((j * (self.icon_size + self.line_size) + self.line_size,
                                      i * (self.icon_size + self.line_size) + self.line_size))
                self.blit_alpha(screen, img, square, alpha)

    @staticmethod
    def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = _.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)
