from typing_extensions import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # single element just return null
        if not head.next and n==1:
            return head.next

        # use fast and slow pointers to count the number of nodes in the list
        fast, slow = head, head
        count = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        
        # odd amount of elements
        if fast and slow.next:
            count = 2 * count - 1
        elif slow.next:
            # even amount of elements
            count = 2 * count - 2
        
        # just delete the head node
        if n == count:
            return head.next

        # delete the required node if not the first one
        temp = head
        for i in range(0, count):
            if i + 1 == (count - n) and temp.next:
                temp.next = temp.next.next
                return head
            temp = temp.next
            