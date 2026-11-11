144. Binary Tree Preorder Traversal

In this problem we need to traverse Binary Tree in Preorder way and then return values of nodes

I solved this task by using recursion. First defined variable node_vals = [] to collect values in correct order. Then using new function
traverse, here first list.append(current node value), then called traverse(left) recursively, so again traverse(right).
If node is None we just return.
