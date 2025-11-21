"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        g = {}
        g[node] = Node(node.val)
        q = deque([node])

        while q:
            current = q.popleft()
            print(f"processing {current.val}")
            for n in current.neighbors:
                if n not in g:
                    g[n] = Node(n.val)
                    q.append(n)
                g[current].neighbors.append(g[n])
        
        return g[node]
        