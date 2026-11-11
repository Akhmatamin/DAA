226. Invert Binary Tree

Here we need to invert the binary tree, it means that left and right children of every node must be swapped

I solved this task by using recursion. If node is None return None, and if node is leaf we just return it.
Otherwise swap root.left and root.right, then call invertTree for left subtree and for right subtree, and at the end return root.
