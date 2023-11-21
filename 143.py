from typing_extensions import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
The idea here is using 3 steps
First use fast and slow pointer technique to cleave the list in half

Then reverse the pointers of the second half of the list

Then iterate over the head in the first half and the tail in the second half
To match corresponding elements together

"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # nothing to be done here
        if head is None or head.next is None: return

        # fast slow pointers technique
        # after this slow will contain the middle element of the list
        # this will either be the middle element if the list is odd in length
        # or the second middle element if the list is even in length
        slow, fast = head, head
        while fast and fast.next:          
            slow = slow.next
            fast = fast.next.next


        
        # now slow contains the middle node
        # using this prev , reverse the pointers of each of the nodes in the second half
        prev = None
        while slow:
            # keeping track of next node
            temp = slow.next

            # assing new next pointer
            slow.next = prev
            
            # next node's prev
            prev = slow
            # moving along the rest of the list

            # moving slow pointer along list
            slow = temp
        
        # prev now contains the start of the reversed second half (aka the tail)

        # we are going to keep inserting elements in the first half of the list from the second half of the list
        while prev.next:
            # Store the next nodes for head and prev
            next_head = head.next  
            next_prev = prev.next  
            
            # Insert tail node after head and add the rest of the head list after the new node
            head.next = prev 
            head.next.next = next_head 
            
            # move pointers to their saved positions
            head = next_head  
            prev = next_prev  

        
