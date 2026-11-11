111. Minimum Depth of Binary Tree

Here we need to find minimum depth of the binary tree, it is number of nodes on the shortest path from root to the nearest leaf

I solved this task by using recursion. If node is None it returns 0. Important thing is that if one child is missing
we cant take min, because None gives 0 and it is not a leaf. So if there is no right child return 1 + minDepth(left),
if no left child return 1 + minDepth(right). If both children exist return 1 + min of left and right.

Time complexity: O(n), where n is number of nodes.
Why: in worst case we must check every node, because we dont know where the nearest leaf is. Each call does only O(1) work (a comparison and addition), and each node is called one time. So O(n).

Space complexity: O(h), where h is height of tree, because of recursion stack. Worst case O(n) for tree like a line, O(log n) for balanced tree.
