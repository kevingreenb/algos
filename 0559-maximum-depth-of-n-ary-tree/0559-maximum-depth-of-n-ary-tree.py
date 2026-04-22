"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = deque([root])
        ans = 0
        while q:
            ans += 1
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                for child in cur.children:
                    if child:
                        q.append(child)
        return ans