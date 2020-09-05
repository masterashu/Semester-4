# Artificial Intelligence
## Assignment 2
<div style="text-align: center;"> by Ashutosh Chauhan</div>

### List of Games:
The following games have been implemented. To see the implementation
visit the respective file.
* [Tic Tac Toe (tictactoe.py)](tictactoe.py) 
* [Open Field Tic Tac Toe (openfield_tictactoe.py)](openfield_tictactoe.py)

### List of Algorithms:
The following algorithms are implemented:
* Standard Min-Max
* Min Max with *alpha* *beta* pruning
* Min Max with limited depth
* Min Max with limited depth and *alpha* *beta* pruning
* Using a custom heuristic function to improve the searching algorithm

All the search algorithms are implemented in the [minmax.py](minmax.py) file.

### Game Solving Agents and Game Playing Agents
The `GameSolvingAgent` which is use to predict
moves and make changes to the game state.  
The `GamePlayingAgent` exposes API to accept
and verify user input and print game state.  
Both the agents are defined in the [game.py](game.py)

### Interactive UI
[pygame](https://pypi.org/project/pygame) library was used to create a
minimal interactive *(**click** to make your move)* UI frontend for the 
`GamePlayingAgent`. The `GameRunner` class manages all the UI interface 
and is present in [game_runner.py](game_runner.py)

> Note: Install pygame dependency using:  
> ```pip3 install pygame```

### Running the game:
#### Step 1: Initialize a game object
```python
from tictactoe import TicTacToe
t = TicTacToe()
```

#### Step 2: Initialize the GameRunner object with the game:
```python
from game_runner import GameRunner, Algorithm
g = GameRunner(game=t, algo=Algorithm.MinMax)
# Other information about the GameRunner class is mentioned
# in the Jupyter Notebook file.
```

#### Step 3: Start the game
```python
# Use the start method of the GameRunner class to start the game
g.start()
```

