# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {num : i for i, num in enumerate(inorder)}
        self.pre = 0

        def build(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[self.pre])
            mid = inorder_map[preorder[self.pre]]
            self.pre += 1
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(preorder)-1)
        