# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque([(root, root.val)])

        while q:
            current, total = q.popleft()
            if total == targetSum and not current.left and not current.right:
                return True
            if current.left:
                q.append((current.left, current.left.val + total))
            if current.right:
                q.append((current.right, current.right.val + total))
        
        return False