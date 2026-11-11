226. Invert Binary Tree

Here we need to invert the binary tree, it means that left and right children of every node must be swapped

I solved this task by using recursion. If node is None return None, and if node is leaf we just return it.
Otherwise swap root.left and root.right, then call invertTree for left subtree and for right subtree, and at the end return root.

Time complexity: O(n), where n is number of nodes.
Why: invertTree is called one time for each node, and in each call we only swap two pointers, it is O(1). So O(n) in total.

Space complexity: O(h), where h is height of tree. We dont create new nodes, only recursion stack is used. In worst case (tree like a line) h = n so O(n), for balanced tree it is O(log n).
