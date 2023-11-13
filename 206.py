# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Better Solution

        # prev keeps track of the previous element
        # curr keeps track of the current element
        prev, curr = None, head

        # while there is a current element
        while curr:
            # keep track of next element
            nxt = curr.next
            
            # switch the next pointer to the previous value
            curr.next = prev

            # making current element the new previous value
            prev = curr

            # incrementing the curr pointer
            curr = nxt
        
        # prev now contains the reversed linked list with the last element as the head
        return prev

        # Original Solution, make a new list while iterating
        # if not head:
        #     return

        # node = head
        # tail = ListNode(head.val)
        # while node.next:
        #     tail = ListNode(node.next.val, tail)
        #     node = node.next
        # return tail
