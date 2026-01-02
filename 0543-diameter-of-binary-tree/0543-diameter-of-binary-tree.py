# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def dfs(root, ans):
#             if not root:
#                 return 0
#             left = dfs(root.left, ans)
#             right = dfs(root.right, ans)
#             ans[0] = max(ans[0],left+right)
#             return max(left, right) + 1

#         ans = [0]
#         dfs(root,ans)
#         return ans[0]

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans,left+right)
            return max(left, right) + 1

        dfs(root)
        return self.ans

        