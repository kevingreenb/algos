# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        def helper(root):
            if not root:
                return 0
            l = max(helper(root.left), 0)
            r = max(helper(root.right), 0)
            cur = root.val + l + r
            self.ans = max(self.ans, cur)
            return root.val + max(l, r)
        helper(root)
        return self.ans