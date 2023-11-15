# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Solution 2(Better): Utilizes fast and head pointers
        If fast ever 'laps' head, then there is a cycle
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        """
        Solution 1: exploits the constraints of the problem
        if our counter passes the maximum number of nodes there is a cycle
        """
        # max_val = 10**4

        # curr = head
        # num = 0
        # while curr:
        #     curr = curr.next
        #     num += 1
        #     if num == max_val + 1:
        #         return True
        # return False