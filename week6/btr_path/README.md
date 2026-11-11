257. Binary Tree Paths

In this problem we need to return all paths from root to leaves as strings like "1->2->5"

I solved this task by using recursion. First if root is empty return empty list. Then defined result = [] and function traverse(node, curr_path).
In it we add current node value to curr_path (with '->' if path is not empty). If the node is leaf (no left and no right child)
we append curr_path to result and return. Otherwise we call traverse for left and then for right.

Time complexity: O(n^2) in worst case (n is number of nodes).
Why: we visit every node one time, it is O(n) visits. But on every node we make new string curr_path += '->' + str(node.val), and strings are copied, so it costs as long as the path length. In tree like a line path length can be up to n, so n * n = O(n^2). For balanced tree path is only about log n, so it is faster there.

Space complexity: O(n) for recursion stack in worst case (O(h) where h is height), plus result list which stores all paths strings, in worst case it can be bigger than that because every path is a separate string.
