141. Linked List Cycle

In this problem we need to find if there is node pointing to back another node
or in another word node.next -> previous nodes
To implement it i used set to store nodes that i went thorough(it can store unique objects)
For each node:
If it is already in the set, a cycle exists, return true.
Otherwise, add it to the set and continue.

Time complexity O(n)