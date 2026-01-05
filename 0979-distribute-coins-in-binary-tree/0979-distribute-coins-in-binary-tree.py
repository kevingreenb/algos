# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            
            # Calculate excess coins from left and right children
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            # The number of moves is the total "flow" through this node
            self.moves += abs(left_excess) + abs(right_excess)
            
            # Return the net balance of this node to its parent:
            # (Current coins + coins from children) - 1 (the coin this node keeps)
            return node.val + left_excess + right_excess - 1

        dfs(root)
        return self.moves