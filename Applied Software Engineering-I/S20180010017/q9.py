#!/bin/python3
# Is this a tree?

import math
import os
import random
import re
import sys

# Answer
from typing import List
class E1(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    name = 'E1'
    what = 'More than 2 children'

class E2(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    name = 'E2'
    what = 'Duplicate Edges'

class E3(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    name = 'E3'
    what = 'Cycle present'

class E4(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    name = 'E4'
    what = 'Multiple roots'

class E5(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    name = 'E5'
    what = 'Any other error'

def parseNodesStr(nodesStr: str):
    import re
    regexp = r'\((\w),(\w)\)'
    roots = []
    edges = []

    for i in re.findall(regexp, nodesStr):
        a,b = i
        # using node to find the root parent
        if a not in roots:
            roots.append(a)

        if b in roots:
            roots.remove(b)

        if (a,b) in edges:
            raise E2()
        edges.append((a,b))
    
    # Extra care
    for a,b in edges:
        if b in roots:
            roots.remove(b)

    if not roots:
        raise E3
    if len(roots) != 1:
        from collections import defaultdict
        # checks for multiple children
        count = defaultdict(int)
        for a,b in edges:
            count[a] += 1
        if max(map(lambda x: count[x], count.keys())) > 2:
            raise E1
        raise E4

    return roots.pop(), edges

class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left or None
        self.right = right or None
        self.parent = parent or None

    def __str__(self):
        s = ''
        if self.val == None:
            return
        s += self.val
        if self.left:
            s += str(self.left)        
        if self.right:
            s += str(self.right)        
        return f'({s})'
        

class Tree:
    def __init__(self, root, edges):
        # Lexicographically smallest root
        self.root:Node = Node(root)
        self.edges:list = edges
        self.nodes:List<Node>() = [self.root]

    def find_node(self, val):
        for i in self.nodes:
            if i.val == val:
                return i
        return None
    
    def generate_tree(self):
        for (a,b) in self.edges:
            if self.find_node(a):
                parent = self.find_node(a)
            else:
                parent = Node(a)
                self.nodes.append(parent)

            if self.find_node(b):
                child = self.find_node(b)
            else:
                child = Node(b)
                self.nodes.append(child)
        
            if child.parent:
                raise E3

            if parent.left == None:
                parent.left = child
            elif parent.left.val > child.val:
                parent.right = parent.left
                parent.left = child
            elif parent.right is None:
                parent.right = child
            else:
                raise E1

            child.parent = parent

    def __str__(self):
        return str(self.root)
    

def sExpression(nodes: str) -> str:
    try:
        root, edges = parseNodesStr(nodes)
        tree = Tree(root, edges)
        tree.generate_tree()
        return str(tree)
    except Exception as e:
        return e.name

if __name__ == '__main__':

    nodes = input()

    result = sExpression(nodes)

    print(result + '\n')
