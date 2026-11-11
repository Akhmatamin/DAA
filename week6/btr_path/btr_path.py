class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathTree(self, root: TreeNode) -> list:
        if not root:
            return []
        
        result = []

        def traverse(node, curr_path):
            if not node:
                return

            if curr_path:
                curr_path += '->' + str(node.val)
            else:
                curr_path = str(node.val)

            if not node.left and not node.right:
                result.append(curr_path)
                return

            traverse(node.left, curr_path)
            traverse(node.right, curr_path)

        traverse(root, "")
        return result