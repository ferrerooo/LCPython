"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return None

        d = {}
        visited = set()
        q = deque()

        q.append(node)

        while len(q) > 0:
            curnode = q.popleft()
            if curnode in visited:
                continue
            visited.add(curnode)
            if curnode not in d:
                d[curnode] = Node(curnode.val)
            newnode = d[curnode]

            for n in curnode.neighbors:
                if n not in d:
                    d[n] = Node(n.val)
                newnode.neighbors.append(d[n])
                if n not in visited:
                    q.append(n)
        
        return d[node]
