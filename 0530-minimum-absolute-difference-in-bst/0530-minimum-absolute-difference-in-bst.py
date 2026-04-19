# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        node = root
        ans = float('inf')
        prev = None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None:
                ans = min(ans, abs(node.val - prev))
            prev = node.val
            node = node.right
        
        return ans