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

        g = { node : Node(node.val) }
        q = deque([node])

        while q:
            current = q.popleft()

            for nei in current.neighbors:
                if nei not in g:
                    g[nei] = Node(nei.val)
                    q.append(nei)
                g[current].neighbors.append(g[nei])

        return g[node]    
        