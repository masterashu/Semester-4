from game import Game, Player
from copy import deepcopy


def _initial_state_tic_tac_toe(board_size: int):
    return [[' ' for _ in range(board_size)] for _ in range(board_size)]


def _all_moves_tic_tac_toe(board_size: int):
    marks = ['O', 'X']
    positions = [(i, j) for i in range(1, board_size + 1)
                 for j in range(1, board_size + 1)]
    return set((m, i, j) for m in marks for (i, j) in positions)


def _players_tic_tac_toe():
    return [Player("Player 1", "O"), Player("Player 2", 'X', True)]


class OpenFieldTicTacToe(Game):
    def __init__(self, initial_state=None,
                 all_moves=None,
                 players=None,
                 board_size: int = 6,
                 win_length: int = 4):

        if not initial_state:
            initial_state = _initial_state_tic_tac_toe(board_size)
        if not all_moves:
            all_moves = _all_moves_tic_tac_toe(board_size)
        if not players:
            players = _players_tic_tac_toe()

        super(OpenFieldTicTacToe, self).__init__(
            initial_state, all_moves, players)

        self.state = deepcopy(initial_state)
        self._board_size = board_size
        self._win_length = win_length

    def make_move(self, move):
        self.state = self.transition(self.state, move)

    def heuristic(self, state):
        L = len(state)
        m = self.players[0].mark
        score = 0
        # Possible Horizontal
        for i in range(L):
            count = 0
            for j in range(L):
                if state[i][j] == m:
                    count += 100
                elif state[i][j] == ' ':
                    count += 15
                else:
                    count = -25
                    break
            score += count

        # Possible Vertical
        for i in range(L):
            count = 0
            for j in range(L):
                if state[j][i] == m:
                    count += 100
                elif state[j][i] == ' ':
                    count += 15
                else:
                    count = -25
                    break
            score += count

        # Possible Diagonal
        for i in range(self._board_size):
            for j in range(self._board_size):
                count = 0
                for k in range(self._board_size - i - j):
                    if state[i + k][j - k] == m:
                        count += 100
                    elif state[i + k][j - k] == ' ':
                        count += 15
                    else:
                        count = -25
                        break
                score += count

        count = 0
        for i in range(self._board_size):
            for j in range(self._board_size):
                count = 0
                for k in range(self._board_size - i - j):
                    if state[i + k][L - k - j - 1] == m:
                        count += 100
                    elif state[i + k][L - k - j - 1] == ' ':
                        count += 15
                    else:
                        count = -25
                        break
                score += count

        return score

    def utility(self, state, player: Player):
        w = self.winner(state)

        # Cannot find utility of a game in progress
        assert (w != "Game Not Ended")

        if w == "TIE":
            return 0
        elif w == player.mark:
            return float('inf')
        else:
            return float('-inf')

    def explore_moves(self, state, player: Player):
        moves = []
        for mark, i, j in self.all_moves:
            if state[i - 1][j - 1] == ' ' and mark == player.mark:
                moves.append((mark, i, j))
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

    def game_end(self, state):
        return self.winner(state) not in ["Game Not Ended"]

    def winner(self, state):
        w = self._winner(state)
        if w is not None:
            return w

        x = []
        for i in state:
            x += i

        if ' ' in x:
            return "Game Not Ended"
        else:
            return "TIE"

    def _winner(self, state):
        # for each player
        for p in self.players:

            # Horizontal
            for i in range(self._board_size):
                count = 0
                for j in range(self._board_size):
                    count = (count + 1) if state[i][j] == p.mark else 0
                    if count >= self._win_length:
                        return p.mark

            # Vertical
            for i in range(self._board_size):
                count = 0
                for j in range(self._board_size):
                    count = (count + 1) if state[j][i] == p.mark else 0
                    if count >= self._win_length:
                        return p.mark

            # Diagonal
            for i in range(self._board_size):
                for j in range(self._board_size):
                    count = 0
                    for k in range(self._board_size - i - j):
                        count = (
                                count + 1) if state[i + k][j + k] == p.mark else 0
                        if count >= self._win_length:
                            return p.mark

            for i in range(self._board_size):
                for j in range(self._board_size):
                    count = 0
                    for k in range(self._board_size - i - j):
                        if state[i + k][self._board_size - j - k - 1] == p.mark:
                            count = (count + 1)
                        else:
                            count = 0
                        if count >= self._win_length:
                            return p.mark

        return None

    @staticmethod
    def get_user_move(player: Player):
        i, j = map(int, input(
            "Enter Input Position (top left is 1, 1): ").split())
        return player.mark, i, j

    def reset(self):
        self.initial_state = _initial_state_tic_tac_toe(self.board_size)
        self.state = _initial_state_tic_tac_toe(self.board_size)
        self.all_moves = _all_moves_tic_tac_toe(self.board_size)
        self.players = _players_tic_tac_toe() 
    
    def state_repr(self, state):
        s = []
        for i in state:
            s.append(' | '.join(i))
        s = ('\n' + '-' * (len(i) * 4 - 3) + '\n').join(s)
        return s
