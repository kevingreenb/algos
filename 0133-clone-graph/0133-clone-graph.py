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
        graph = {node : Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in graph:
                    graph[n] = Node(n.val)
                    q.append(n)
                graph[cur].neighbors.append(graph[n])
        return graph[node]
        