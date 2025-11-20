# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            current = []
            size = len(q)
            for _ in range(size):
                c = q.popleft()
                current.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            ans.append(current)
        return ans