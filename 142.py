# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow fast approach to determine a cycle
        # if there is a cycle, save the spot where the pointers meet and break the loop
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        # once out of the loop increment from the head and meeting place
        # until both are equal
        # when they are equal, we have discovered the beginning of the cycle
        p1, p2 = head, slow
        while p1!=p2:
            p1, p2 = p1.next, p2.next
        return p1