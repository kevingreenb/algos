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
        old_to_new = {node : Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in old_to_new:
                    old_to_new[n] = Node(n.val)
                    q.append(n)
                old_to_new[cur].neighbors.append(old_to_new[n])
        return old_to_new[node]
        