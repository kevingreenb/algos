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

        def is_leaf(root):
            return not root.left and not root.right

        def backtrack(root):
            cur.append(str(root.val))
            if is_leaf(root):
                ans.append("->".join(cur))
            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            cur.pop()
            

        backtrack(root)
        return ans
        