145. Binary Tree Postorder Traversal

In this problem we need to traverse Binary Tree in Postorder way and then return values of nodes

I solved this task by using recursion. First defined variable node_vals = [] to collect values in correct order. Then using new function
traverse, here first called traverse(left) recursively, then traverse(right), so only after both of them list.append(current node value).
If node is None we just return.
