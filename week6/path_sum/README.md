112. Path Sum

Here we need to check if the tree has root-to-leaf path where sum of all node values is equal to given sum

I solved this task by using recursion. If node is None return False. If node is leaf (no left and no right) we check
root.val == sum. Otherwise we call hasPathSum for left and right with sum - root.val (we subtract current value),
and use or, because it is enough that one of paths works.

Time complexity: O(n), where n is number of nodes.
Why: in worst case there is no good path (or it is the last one), so we visit every node one time. In each call we do only a subtraction and comparison, it is O(1). The or can stop early if left path is True, but worst case is still O(n).

Space complexity: O(h), where h is height of tree, because of recursion stack. Worst case O(n) for tree like a line, O(log n) for balanced tree.
