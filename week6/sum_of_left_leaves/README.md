404. Sum of Left Leaves

Here we need to return sum of values of all left leaves in the tree (leaf is node without children, and it must be left child)

I solved this task by using recursion. If node is None return 0. Defined variable total = 0. If root.left exists and it has no
children (left leaf) we add its value to total. Then we add results of sumOfLeftLeaves for left and right subtrees and return total.

Time complexity: O(n), where n is number of nodes.
Why: sumOfLeftLeaves is called one time for every node, and inside we only check left child and add numbers, it is O(1) work. So O(n).

Space complexity: O(h), where h is height of tree, because of recursion stack. Worst case O(n) for tree like a line, O(log n) for balanced tree.
