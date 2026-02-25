# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.ans = 0

        def helper(root, max_val):
            if not root:
                return 0

            if root.val >= max_val:
                self.ans +=1
                max_val = root.val

            helper(root.left, max_val)
            helper(root.right, max_val)
            
        helper(root, root.val)
        return self.ans
        