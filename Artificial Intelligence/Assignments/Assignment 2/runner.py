from openfield_tictactoe import *
from game import *
from enum import Enum


class Turn(Enum):
    User = 1
    Computer = 2


if __name__ == "__main__":
    t = OpenFieldTicTacToe(board_size=3, win_length=3)
    agent = GamePlayingAgent(game=t, algo=Algorithm.MinMax)
    turn = Turn.User
    while not agent.game_ended:
        print(agent.game_state)

        if turn == Turn.User:
            try:
                agent.request_input()
            except AssertionError:
                print("Wrong Move!")
                continue
        elif turn == Turn.Computer:
            agent.play()

        turn = Turn.Computer if turn == Turn.User else Turn.User

    print(agent.game_state)
    agent.print_result()
