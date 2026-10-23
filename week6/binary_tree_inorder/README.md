94. Binary Tree Inorder Traversal

In this problem we need to traverse Binary Tree in Inorder way and then return values of nodes

I solved this task by using recursion and list's (stack capability).
First defined variable node_values : [] to collect in correct order values. Then using new function 
/traverse, here first called function recursively traverse(left) then list.append(current node value)
, so again traverse(right)