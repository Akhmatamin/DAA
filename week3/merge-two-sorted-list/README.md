21. Merge Two Sorted Lists

In this problem we need to merge two sorted linked lists into one linked list
To implement solution we need to just compare value of both lists with each other and move pointers further
For example list1.val <= | >= list2.val and then move .next. But before we need to create one dummy object and current pointer to assign nodes

Time complexity is O(n+m) because there is two different lists and we go though them