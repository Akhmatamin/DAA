257. Binary Tree Paths

In this problem we need to return all paths from root to leaves as strings like "1->2->5"

I solved this task by using recursion. First if root is empty return empty list. Then defined result = [] and function traverse(node, curr_path).
In it we add current node value to curr_path (with '->' if path is not empty). If the node is leaf (no left and no right child)
we append curr_path to result and return. Otherwise we call traverse for left and then for right.
