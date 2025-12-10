# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def helper(root):
            if not root:
                return 0
            nonlocal ans
            l = max(helper(root.left),0)
            r = max(helper(root.right),0)
            cur = root.val + l + r
            ans = max(ans, cur)

            return root.val + max(l, r)

        helper(root)
        return ans
        