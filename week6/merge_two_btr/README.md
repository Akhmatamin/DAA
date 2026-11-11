617. Merge Two Binary Trees

Here we need to merge two binary trees, if two nodes are in the same place we sum their values, if only one exists we take it

I solved this task by using recursion. If root1 is None return root2, and if root2 is None return root1.
Otherwise add root2.val to root1.val, then root1.left = mergeTrees(root1.left, root2.left) and
root1.right = mergeTrees(root1.right, root2.right). At the end return root1 (so we reuse the first tree and dont create new nodes).

Time complexity: O(min(n, m)), where n and m are sizes of the two trees.
Why: we go down only while both trees have node in the same place. When one of them is None we return the other tree immediately without going inside it. So we visit only overlapping nodes, and it is not more than the smaller tree.

Space complexity: O(min(h1, h2)) for recursion stack, worst case O(min(n, m)). We dont create new nodes because we reuse root1.
