from typing_extensions import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy node helps us handle reversing the first node's pointer
        dummy = ListNode(0, head)
        
        # the group of size k after groupPrev needs to be reversed
        groupPrev = dummy

        while True:
            k_node = self.getKthNode(groupPrev, k)
            if not k_node:
                break
            groupNext = k_node.next
            # reverse group
            # prev is k_node.next because the first node in the group will have the next pointer updated to that
            # curr is groupPrev.next because that is the first node in the group
            prev, curr = k_node.next, groupPrev.next
            
            # reversing the pointers of the linked group
            while curr != groupNext:
                tmp = curr.next # stores next node
                curr.next = prev # flips pointers
                prev = curr # updates previous pointer
                curr = tmp # next iteration

            # tmp holds the initial first node of the group (now technically the last node)
            tmp = groupPrev.next

            # the next '1st node' should now be the kth node, because it has been properly reversed
            groupPrev.next = k_node

            # move group previous to the last node of the group
            groupPrev = tmp

        return dummy.next
    def getKthNode(self, curr, k):
        """
        Get the Kth Node from node curr
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr