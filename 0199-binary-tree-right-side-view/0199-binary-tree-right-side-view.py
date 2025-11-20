# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                c = q.popleft()
                if i == size-1:
                    ans.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
        return ans
        