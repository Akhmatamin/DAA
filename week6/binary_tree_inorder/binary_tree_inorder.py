from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node_values = []

        def traverse(node: TreeNode):
            if not node:
                return

            traverse(node.left)
            node_values.append(node.val)
            traverse(node.right)

        traverse(root)
        return node_values
