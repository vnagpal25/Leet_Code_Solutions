# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast head moves twice as fast as slow head
        slow, fast = head, head

        # when fast head reaches the end, or it is one past the end(null)
        # slow has reached the middle element (if odd number of elements)
        # or the second middle element (if even number of elements)
        # then we can just return slow
        
        # picture diagram of list helps to understand
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        """
        Brute Force Solution iterates through this list twice
        """
        # '''
        # Calculate the length of the list
        # '''
        # curr = head
        # length = 0
        # while curr:
        #     length += 1
        #     curr = curr.next

        # '''
        # Calculate the middle index of the list
        # If the length is odd, the floor rounds down to get the middle index
        # If the length is even, floor has no effect and this gets the second middle element
        # '''
        # middle = math.floor(length / 2)

        # '''
        # Iterate until we reach the middle element, then return it
        # '''
        # curr = head
        # num = 0
        # while curr:
        #     if num == middle:
        #         return curr
        #     num += 1
        #     curr = curr.next
        