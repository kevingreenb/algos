# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans, cur = [], []

        def backtrack(root):
            cur.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->".join(cur))
                cur.pop()
                return
            
            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            cur.pop()
            

        backtrack(root)
        return ans
        