from game import Game, Player
from copy import deepcopy


def _initial_state_tic_tac_toe():
    return [[' ' for _ in range(3)] for _ in range(3)]


def _all_moves_tic_tac_toe():
    marks = ['O', 'X']
    positions = [(i, j) for i in range(1, 4) for j in range(1, 4)]
    return set((m, i, j) for m in marks for (i, j) in positions)


def _players_tic_tac_toe():
    return [Player("Player 1", "O"), Player("Player 2", 'X', True)]


class TicTacToe(Game):
    def __init__(self, initial_state=None,
                 all_moves=None,
                 players=None):

        if not initial_state:
            initial_state = _initial_state_tic_tac_toe()
        if not all_moves:
            all_moves = _all_moves_tic_tac_toe()
        if not players:
            players = _players_tic_tac_toe()

        super(TicTacToe, self).__init__(initial_state, all_moves, players)
        self.state = deepcopy(initial_state)
   
    def make_move(self, move) -> bool:
        try:
            self.state = self.transition(self.state, move)
        except AssertionError:  # Wrong/Illegal Move
            return False
        return True

    def utility(self, state, player: Player):
        _winner = self.winner(state)

        # Cannot find utility of a game in progress
        assert (_winner != "Game Not Ended")

        if _winner == "TIE":
            return 1
        elif _winner == player.mark:
            return 2
        else:
            return 0

    def heuristic(self, state):
        m = self.players[0].mark
        score = 0
        # Possible Horizontal
        for i in range(3):
            count = 0
            for j in range(3):
                if state[i][j] == m:
                    count += 100
                elif state[i][j] == ' ':
                    count += 25
                else:
                    count = -3
                    break
            score += count

        # Possible verticle
        for i in range(3):
            count = 0
            for j in range(3):
                if state[j][i] == m:
                    count += 100
                elif state[j][i] == ' ':
                    count += 25
                else:
                    count = -3
                    break
            score += count

        # Possible Diagonal
        count = 0
        for i, j in [(0, 0), (1, 1), (2, 2)]:
            if state[i][j] == m:
                count += 100
            elif state[i][j] == ' ':
                count += 25
            else:
                count = -3
                break
        score += count
        count = 0
        for i, j in [(0, 2), (1, 1), (2, 0)]:
            if state[i][j] == m:
                count += 100
            elif state[i][j] == ' ':
                count += 25
            else:
                count = -3
                break
        score += count
        return score

    def explore_moves(self, state, player: Player):
        moves = []

        for mark, i, j in self.all_moves:
            if state[i - 1][j - 1] == ' ' and player.mark == mark:
                moves.append((player.mark, i, j))

        return moves

    @staticmethod
    def transition(state, move, player=None):
        mark, i, j = move

        # Check for an Invalid Move
        assert (state[i - 1][j - 1] == ' ')
        assert (player is None or player.mark == mark)

        new_state = deepcopy(state)
        new_state[i - 1][j - 1] = mark

        return new_state

    def game_end(self, state) -> bool:
        return self.winner(state) != "Game Not Ended"

    def winner(self, state):
        if state[1][1] != ' ':
            if state[0][0] == state[2][2] == state[1][1] or state[0][1] == state[2][1] == state[1][1] or state[1][0] == \
                    state[1][2] == state[1][1] or state[2][0] == state[0][2] == state[1][1]:
                return state[1][1]

        if state[0][0] != ' ':
            if state[0][0] == state[0][2] == state[0][1] or state[0][0] == state[2][0] == state[1][0]:
                return state[0][0]

        if state[2][2] != ' ':
            if state[2][0] == state[2][1] == state[2][2] or state[0][2] == state[1][2] == state[2][2]:
                return state[2][2]

        if ' ' in (state[0] + state[1] + state[2]):
            return "Game Not Ended"

        else:
            return "TIE"

    @staticmethod
    def get_user_move(player: Player):
        i, j = map(int, input(
            "Enter Input Position (top left is 1, 1): ").split())
        return player.mark, i, j
     
    def reset(self):
        self.initial_state = _initial_state_tic_tac_toe()
        self.state = _initial_state_tic_tac_toe()
        self.all_moves = _all_moves_tic_tac_toe()
        self.players = _players_tic_tac_toe() 
        
    def state_repr(self, state):
        s = ''
        for i in state:
            s += ' | '.join(i)
            s += '\n' + '-' * (len(i) * 4 - 3)
        return s
