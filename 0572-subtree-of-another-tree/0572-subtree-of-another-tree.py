class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p or not q:
                return p is q
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)