from game_runner import TicTacToe, OpenFieldTicTacToe, GameRunner, Algorithm

# Main
if __name__ == '__main__':
    # g = OpenFieldTicTacToe(board_size=4, win_length=4)
    g = TicTacToe()
    x = GameRunner(game=g, algo=Algorithm.MinMax, max_depth=6)
    x.start()
