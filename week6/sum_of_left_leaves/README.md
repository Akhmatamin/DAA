404. Sum of Left Leaves

Here we need to return sum of values of all left leaves in the tree (leaf is node without children, and it must be left child)

I solved this task by using recursion. If node is None return 0. Defined variable total = 0. If root.left exists and it has no
children (left leaf) we add its value to total. Then we add results of sumOfLeftLeaves for left and right subtrees and return total.
