145. Binary Tree Postorder Traversal

In this problem we need to traverse Binary Tree in Postorder way and then return values of nodes

I solved this task by using recursion. First defined variable node_vals = [] to collect values in correct order. Then using new function
traverse, here first called traverse(left) recursively, then traverse(right), so only after both of them list.append(current node value).
If node is None we just return.

Time complexity: O(n), where n is number of nodes.
Why: every node is visited exactly one time by traverse (left, right, then append), and append is O(1). None children just return. So total O(n).

Space complexity: O(n). List node_vals keeps all n values. Recursion stack takes O(h), where h is height, worst case O(n) for a tree like a line.
