# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # slow pointer will contain the second middle element at the end
        # fast pointer controls the slow pointer's position
        slow, fast = head, head

        # prev pointer will contain the second middle element at the end
        prev = None # keeps track of the current previous pointer

        """
        The fast pointer ensures that when fast reaches the end of the list
        our slow pointer reaches the middle of the list

        The idea here is to split the list into 2 halves
        For the first half, we want to essentially flip the pointers

        This way we can iterate through the first half backwards at the same time as we iterate through the second half forwards(unchanged)

        Then we can determine the max sum
        """
        while fast and fast.next:
            # update fast pointer
            fast = fast.next.next

            #  placeholder for slow's next position
            temp = slow.next
            
            # reverse the next pointer
            # and update the prev pointer
            slow.next = prev
            prev = slow

            # use the placeholder to update slow to its adjacent right element
            slow = temp
        

        """
        Now slow contains the second middle element
        and prev contains the first middle element (but the pointers are flipped)
        """
        res = 0
        while slow and prev:
            # update the maximum sum 
            res = max(res, slow.val + prev.val)
            
            # move through first half backwards and second half forwards
            slow, prev = slow.next, prev.next
        
        return res
        