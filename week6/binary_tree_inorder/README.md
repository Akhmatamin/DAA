94. Binary Tree Inorder Traversal

In this problem we need to traverse Binary Tree in Inorder way and then return values of nodes

I solved this task by using recursion and list's (stack capability).
First defined variable node_values : [] to collect in correct order values. Then using new function 
/traverse, here first called function recursively traverse(left) then list.append(current node value)
, so again traverse(right)
Time complexity: O(n), where n is number of nodes.
Why: traverse is called one time for every node, and for None children it returns right away. Inside we do only append, it is O(1). So work is n times a constant = O(n).

Space complexity: O(n). List node_values keeps all n values. Recursion stack also takes O(h) (h is height of tree), in worst case O(n) if tree is like a line.
