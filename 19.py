from typing_extensions import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution 2, use delayed 2 pointers
        
        # start both at the head
        p1, p2 = head, head
        
        # move the second pointer n nodes from head
        for _ in range(n):
            p2 = p2.next
        
        # if p2 has traversed out of bounds, we know that we just need to remove the first node
        if not p2: 
            return p1.next
        
        # move p2 and p1 until p2 is the tail node
        while p2.next:
            p1, p2 = p1.next, p2.next

        # now the node after p1 is the one that we remove
        p1.next = p1.next.next
        
        return head


        # Solution 1: using fast and slow pointers to count nodes


        # # use fast and slow pointers to count the number of nodes in the list
        # fast, slow = head, head
        # count = 1
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     count += 1
        
        # # odd amount of elements
        # if fast and slow.next:
        #     count = 2 * count - 1
        # elif slow.next:
        #     # even amount of elements
        #     count = 2 * count - 2
        
        # # just delete the head node
        # if n == count:
        #     return head.next

        # # delete the required node if not the first one
        # temp = head
        # for i in range(0, count):
        #     if i + 1 == (count - n) and temp.next:
        #         temp.next = temp.next.next
        #         return head
        #     temp = temp.next
            