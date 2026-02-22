# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root is subRoot
        def is_same(root, subRoot):
            if not root or not subRoot:
                return root is subRoot
            if root.val != subRoot.val:
                return False
            return is_same(root.left, subRoot.left) and is_same(root.right, subRoot.right)
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        