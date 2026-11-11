112. Path Sum

Here we need to check if the tree has root-to-leaf path where sum of all node values is equal to given sum

I solved this task by using recursion. If node is None return False. If node is leaf (no left and no right) we check
root.val == sum. Otherwise we call hasPathSum for left and right with sum - root.val (we subtract current value),
and use or, because it is enough that one of paths works.
