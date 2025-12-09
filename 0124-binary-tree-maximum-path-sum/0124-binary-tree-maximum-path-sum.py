class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        
        def helper(node):
            nonlocal ans
            if not node:
                return 0
                
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)
            path_through_node = node.val + left_gain + right_gain
            ans = max(ans, path_through_node)
            return node.val + max(left_gain, right_gain)
        
        helper(root)
        return ans