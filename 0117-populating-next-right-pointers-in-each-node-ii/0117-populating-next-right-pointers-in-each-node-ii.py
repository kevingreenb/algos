"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        cur = root

        while cur:
            dummy = Node(0)
            pointer = dummy
            while cur:
                if cur.left:
                    pointer.next = cur.left
                    pointer = pointer.next
                if cur.right:
                    pointer.next = cur.right
                    pointer = pointer.next
                
                cur = cur.next
            cur = dummy.next
        return root     