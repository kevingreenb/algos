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
            return None


        curr = root
        while curr:
            dummy = Node(0)
            pointer = dummy
            while curr:
                if curr.left:
                    pointer.next = curr.left
                    pointer = pointer.next
                if curr.right:
                    pointer.next = curr.right
                    pointer = pointer.next
                
                curr = curr.next
            curr = dummy.next
        return root

        

