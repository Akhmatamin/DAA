class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:

        node_vals = []
        def traverse(node: TreeNode):
            if not node:
                return

            node_vals.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return node_vals