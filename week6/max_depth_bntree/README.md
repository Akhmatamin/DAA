104. Maximum Depth of Binary Tree

Here we need to find maximum depth of the binary tree. To solve we use recursion to explore each node
first call maxDepth method for left subtree then right subtree by adding 1 for current node and finding max value for right and left
when there is node = None it return 0 