# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def preorder(node, out):
            if not node:
                out.append('X')
                return
            out.append(',' + str(node.val))
            preorder(node.left, out)
            preorder(node.right, out)

        s_ser = []
        t_ser = []
        preorder(s, s_ser)
        preorder(t, t_ser)

        s_str = ''.join(s_ser)
        t_str = ''.join(t_ser)

        return t_str in s_str
        