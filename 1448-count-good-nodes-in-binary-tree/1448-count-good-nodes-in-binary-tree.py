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
        def dfs(root, max_val):
            if not root:
                return
            if root.val >= max_val:
                max_val = root.val
                self.ans += 1
            dfs(root.left, max_val)
            dfs(root.right, max_val)
        dfs(root, root.val)
        return self.ans