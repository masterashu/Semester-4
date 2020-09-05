from abc import ABC, abstractmethod
from minmax import *
from typing import List


class Player:
    def __init__(self, name='Player', mark=None, user: bool = False):
        self.name = name
        self.mark = mark
        self.user = user

    def __str__(self):
        return f'{self.name} - {self.mark}'


class Game(ABC):
    def __init__(self, initial_state, all_moves, players: List[Player]):
        self.initial_state = initial_state
        self.all_moves = all_moves
        self.players = players
        self.state = None
        super(Game, self).__init__()

    @abstractmethod
    def make_move(self, move) -> bool:
        pass

    @abstractmethod
    def utility(self, state, player):
        pass

    @abstractmethod
    def explore_moves(self, state, player: Player):
        pass

    @staticmethod
    @abstractmethod
    def transition(state, move, player=None):
        pass

    @abstractmethod
    def game_end(self, state) -> bool:
        pass

    @abstractmethod
    def winner(self, state):
        pass

    @staticmethod
    @abstractmethod
    def get_user_move(player):
        pass

    @abstractmethod
    def heuristic(self, state):
        pass

    @abstractmethod
    def state_repr(self, state):
        pass
    
    @abstractmethod
    def reset(self):
        pass


class GameSolvingAgent:
    def __init__(self, game: Game, current_player=None, algo: Algorithm = Algorithm.MinMax):
        self.game = game
        self.moves = []
        self.current_player = current_player or game.players[0]
        self.algo = algo

    def predict_next_move(self, max_depth=5):
        move = search_minmax(self.game, self.algo, max_depth=max_depth)
        return move

    def make_agent_move(self, move):
        self.game.make_move(move)
        self.moves.append(move)

    # Duplicate Function to distinguish
    # user actions from agents without confusion
    def make_user_move(self, user_move):
        self.moves.append(user_move)
        if self.game.make_move(user_move) is False:
            raise AssertionError()


class GamePlayingAgent:
    def __init__(self, game: Game, algo: Algorithm = Algorithm.MinMax, **kwargs):
        self.game = game
        self.algo = algo
        self.params = kwargs
        self.agent = GameSolvingAgent(game, algo=algo)

    @property
    def game_ended(self):
        return self.game.game_end(self.game.state)

    @property
    def game_state(self):
        return self.game.state_repr(self.game.state)

    def play(self):
        _move = self.agent.predict_next_move(**self.params)
        if _move:
            self.agent.make_agent_move(_move)
        else:
            print("No possible Moves")

    def request_input(self):
        player = self.game.players[1]
        # Verify The Player is User
        assert player.user
        _move = self.game.get_user_move(player)
        self.agent.make_user_move(_move)

    def user_move(self, pos):
        player = self.game.players[1]
        move = (player.mark, pos[0], pos[1])
        try:
            self.agent.make_user_move(move)
        except AssertionError:
            return False
        return True

    def print_result(self):
        assert self.game_ended
        if self.game.winner(self.game.state) == "TIE":
            s = "It's a tie."
        else:
            s = self.game.winner(self.game.state) + ' wins'
