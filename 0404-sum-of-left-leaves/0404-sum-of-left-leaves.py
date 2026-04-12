# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        ans = 0
        while q:
            cur, left = q.popleft()
            if left and cur.left is None and cur.right is None:
                ans += cur.val
            if cur.left:
                q.append((cur.left, 1))
            if cur.right:
                q.append((cur.right, 0))

        return ans
        