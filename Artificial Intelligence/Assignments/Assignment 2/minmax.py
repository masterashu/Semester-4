from copy import deepcopy
from enum import Enum


class _MinMax(Enum):
    Min = 1
    Max = 2


class Algorithm(Enum):
    MinMax = 1
    MinMaxWithAphaBetaPruning = 2
    MinMaxWithDepthLimited = 3
    MinMaxWithDepthLimitedAphaBetaPruning = 4
    MinMaxOptimized = 5


def search_minmax(game, algo: Algorithm = Algorithm.MinMax, **kwargs):
    # Check that the first agent is the computer
    #
    # This does not mean that the computer will
    # have the first move
    assert not game.players[0].user
    if algo == Algorithm.MinMax:
        return _minmax(game, deepcopy(game.state), _MinMax.Max)[0]
    elif algo == Algorithm.MinMaxWithAphaBetaPruning:
        return _minmax_alpha_beta(game, deepcopy(game.state), _MinMax.Max, float("-inf"), float("inf"))[0]
    elif algo == Algorithm.MinMaxWithDepthLimited:
        assert ('max_depth' in kwargs)
        return _minmax_depth_limited(game, deepcopy(game.state), _MinMax.Max, max_depth=kwargs['max_depth'])[0]
    elif algo == Algorithm.MinMaxWithDepthLimitedAphaBetaPruning:
        assert ('max_depth' in kwargs)
        return _minmax_depth_limited_alpha_beta(game, deepcopy(game.state),
                                                _MinMax.Max, max_depth=kwargs['max_depth'])[0]
    elif algo == Algorithm.MinMaxOptimized:
        if len(game.state) > 3:
            return _minmax_depth_limited(game, deepcopy(game.state), _MinMax.Max, max_depth=4)[0]
        else:
            return _minmax_alpha_beta(game, deepcopy(game.state), _MinMax.Max, float('-inf'), float('inf'))[0]


def _minmax(game, state, step: _MinMax):
    if game.game_end(state):
        return [None, game.utility(state, game.players[0]) or 0]

    if step is _MinMax.Max:
        moves = game.explore_moves(state, player=game.players[0])
        next_states = list()
        for move in moves:
            a, b = move, _minmax(
                game, game.transition(state, move), _MinMax.Min)[1]
            next_states.append((a, b))
        return max(next_states, key=lambda x: x[1])

    elif step is _MinMax.Min:
        moves = game.explore_moves(state, player=game.players[1])
        next_states = list()
        for move in moves:
            a, b = move, _minmax(
                game, game.transition(state, move), _MinMax.Max)[1]
            next_states.append((a, b))
        return min(next_states, key=lambda x: x[1])


def _minmax_alpha_beta(game, state, step: _MinMax, alpha, beta):
    if game.game_end(state):
        return [None, game.utility(state, game.players[0]) or 0]

    if step is _MinMax.Max:
        best_move = [None, float('-inf')]
        moves = game.explore_moves(state, player=game.players[0])
        assert (len(moves) > 0)
        for move in moves:
            a, b = move, _minmax_alpha_beta(
                game, game.transition(state, move), _MinMax.Min, alpha, beta)[1]
            best_move = max(best_move, (a, b), key=lambda x: x[1])
            alpha = max(alpha, best_move[1])
            if beta <= alpha:
                break
        return best_move

    elif step is _MinMax.Min:
        worst_move = [None, float('+inf')]
        moves = game.explore_moves(state, player=game.players[1])
        assert (len(moves) > 0)
        for move in moves:
            a, b = move, _minmax_alpha_beta(
                game, game.transition(state, move), _MinMax.Max, alpha, beta)[1]
            worst_move = min(worst_move, (a, b), key=lambda x: x[1])
            beta = min(beta, worst_move[1])
            if beta <= alpha:
                break
        return worst_move


def _minmax_depth_limited(game, state, step: _MinMax, max_depth: int, depth: int = 0):
    # player = game.players[0] if step is _MinMax.Max else game.players[1]
    if game.game_end(state):
        return [None, game.utility(state, game.players[0]) or 0]

    if depth >= max_depth:
        return [None, game.heuristic(state)]

    if step is _MinMax.Max:
        moves = game.explore_moves(state, player=game.players[0])
        next_states = list()
        for move in moves:
            a, b = move, _minmax_depth_limited(
                game, game.transition(state, move), _MinMax.Min, max_depth, depth + 1)[1]
            next_states.append((a, b))
        return max(next_states, key=lambda x: x[1])

    elif step is _MinMax.Min:
        moves = game.explore_moves(state, player=game.players[1])
        next_states = list()
        for move in moves:
            a, b = move, _minmax_depth_limited(
                game, game.transition(state, move), _MinMax.Max, max_depth, depth + 1)[1]
            next_states.append((a, b))
        return min(next_states, key=lambda x: x[1])


def _minmax_depth_limited_alpha_beta(game, state, step: _MinMax, max_depth: int, alpha=float("-inf"), beta=float("inf"),
                                     depth: int = 0):
    if game.game_end(state):
        return [None, game.utility(state, game.players[0]) or 0]

    if depth >= max_depth:
        return [None, game.heuristic(state)]

    if step is _MinMax.Max:
        best_move = [None, float('-inf')]
        moves = game.explore_moves(state, player=game.players[0])
        assert (len(moves) > 0)
        for move in moves:
            a, b = move, _minmax_depth_limited_alpha_beta(
                game, game.transition(state, move), _MinMax.Min, max_depth, alpha, beta, depth + 1)[1]
            best_move = max(best_move, (a, b), key=lambda x: x[1])
            alpha = max(alpha, best_move[1])
            if beta <= alpha:
                break
        return best_move

    elif step is _MinMax.Min:
        worst_move = [None, float('inf')]
        moves = game.explore_moves(state, player=game.players[0])
        assert (len(moves) > 0)
        for move in moves:
            a, b = move, _minmax_depth_limited_alpha_beta(
                game, game.transition(state, move), _MinMax.Max, max_depth, alpha, beta, depth + 1)[1]
            worst_move = min(worst_move, (a, b), key=lambda x: x[1])
            beta = min(beta, worst_move[1])
            if beta <= alpha:
                break
        return worst_move
