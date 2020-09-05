#!/bin/python3
# Bob navigates a Maze

import math
import os
import random
import re
import sys

# Answer
from typing import List, Tuple, Dict
from collections import defaultdict
from itertools import permutations
from pprint import pprint


def neighbours(maze: List[List[int]], x, y):
    N, M = len(maze), len(maze[0])
    if x != 0 and maze[x-1][y] != 1:
        yield x-1, y
    if x != N-1 and maze[x+1][y] != 1:
        yield x+1, y
    if y != M-1 and maze[x][y+1] != 1:
        yield x, y+1
    if y != 0 and maze[x][y-1] != 1:
        yield x, y-1
    return


def search_length_bfs(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    visited = []
    to_visit = [(*start, 0)]
    path_cost = float('inf')
    while len(to_visit) > 0:
        x, y, d = to_visit.pop(0)
        visited.append((x, y))
        if (x, y) == end:
            path_cost = d
            break
        for i, j in neighbours(maze, x, y):
            if (i, j) not in visited:
                to_visit.append((i, j, d+1))

    return path_cost


def find_min_path_costs(maze: List[List[int]], points: List[Tuple[int, int]]) -> Dict[Tuple[Tuple[int, int], Tuple[int, int]], int]:
    path_costs = dict()
    for i1, j1 in points:
        for i2, j2 in points:
            if ((i1, j1), (i2, j2)) in path_costs or ((i2, j2), (i1, j1)) in path_costs:
                continue
            if (i1, j1) == (i2, j2):
                path_costs[((i1, j1), (i2, j2))] = 0
            else:
                tmp = search_length_bfs(
                    maze, (i1, j1), (i2, j2))
                path_costs[((i1, j1), (i2, j2))] = tmp
                path_costs[((i2, j2), (i1, j1))] = tmp

    return path_costs


def minMoves(maze: list, x: int, y: int):
    _pos = [(i, j) for i in range(len(maze)) for j in range(len(maze[0]))]
    coins = list(filter(lambda x: maze[x[0]][x[1]] == 2, _pos))
    # print(coins)
    start = (0, 0)
    end = (x, y)
    # Special case
    if not coins:
        cost = search_length_bfs(maze, start, end)
        if cost == float('inf'):
            return -1
        else:
            return cost

    path_cost = find_min_path_costs(maze, [start, *coins, end])
    pprint(path_cost)

    min_cost = float('inf')
    for path in permutations(coins):
        cost = path_cost[(start, path[0])]
        for i in range(len(path)-1):
            cost += path_cost[(path[i], path[i+1])]
            if cost >= min_cost:
                break
        cost += path_cost[(path[-1], end)]
        min_cost = min(cost, min_cost)

    if min_cost == float('inf'):
        return -1
    else:
        return min_cost


if __name__ == '__main__':

    maze_rows = int(input().strip())
    maze_columns = int(input().strip())

    maze = []

    for _ in range(maze_rows):
        maze.append(list(map(int, input().rstrip().split())))

    x = int(input().strip())

    y = int(input().strip())

    result = minMoves(maze, x, y)

    print(str(result) + '\n')
