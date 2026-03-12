# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        self.inorder = []
        self.current = 0
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.inorder.append(node.val)
            node = node.right
        

    def next(self) -> int:
        ans = self.inorder[self.current]
        self.current += 1
        return ans

    def hasNext(self) -> bool:
        return self.current < len(self.inorder)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()