# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_d = {val : i for i, val in enumerate(inorder)}
        self.pre = 0
        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(preorder[self.pre])
            mid = inorder_d[preorder[self.pre]]
            self.pre += 1
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        ans = helper(0, len(inorder) - 1)
        return ans
        