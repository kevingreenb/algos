# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string using preorder traversal."""
        result = []
        
        def preorder(node):
            if not node:
                result.append("N")  # null marker
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        values = iter(data.split(","))
        
        def build():
            val = next(values)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        
        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))