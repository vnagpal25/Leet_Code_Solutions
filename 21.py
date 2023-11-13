from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Recursive approach to merging both lists
consider l1 = [h1|t1]
    and  l2 = [h2|t2]

merged_list = [h1|merge(t1, l2)] if h1 < h2
else
merged_list = [h2|merge(l1, t2)]

merge method has 3 base cases
both are empty, list1 is empty, or list2 is empty

in the first return None (the list is now sorted)
in the second two, return the non empty list (this will be appended to the result)
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not(list1 or list2):
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val > list2.val:
            new_list = ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        else:
            new_list = ListNode(list1.val, self.mergeTwoLists(list1.next, list2))

        return new_list