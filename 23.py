from typing_extensions import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # iterative solution is much more efficient in terms of time and space
    def mergeTwoLists_iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # efficient edge case check
        if not list1:
            return list2
        elif not list2:
            return list1
        
        tail = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case check
        if not lists or len(lists) == 0:
            return None
        
        """
        Basic idea is that we will reducing the length of lists by a factor of 2 each time
        We will do this merging adjacent lists at each iteration
        Once we only have one left, we can just return it
        """
        while len(lists) > 1:
            # will contain the new merged lists
            merged_lists = []

            # merge corresponding pairs of lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                merged_lists.append(self.mergeTwoLists_iterative(l1, l2))
            
            lists = merged_lists

        # return the last list
        return lists[0]
