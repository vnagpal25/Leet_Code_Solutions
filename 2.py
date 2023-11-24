# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """More Efficient 1 pass method"""
        
        # set up pointers for input lists and output lst
        curr1, curr2 = l1, l2
        head = curr = ListNode()

        # define carry for addition
        carry = 0

        # add all of the values where both numbers share a 'place' (i.e. 1's place, 10's place, 100's plae)
        while curr1 and curr2:
            # mod 10 calculates remainder
            # // 10 calculates the carry
            curr.val = (curr1.val + curr2.val + carry) % 10
            carry = (curr1.val + curr2.val + carry) // 10

            # assign the next pointer a ListNode if we have more values to add
            curr.next = ListNode() if (curr1.next or curr2.next or carry) else None
            
            # move pointers along
            curr, curr1, curr2 = curr.next, curr1.next, curr2.next
        
        # add the remaining values from either list with the carry as well
        while curr1:
            # mod 10 calculates remainder
            # // 10 calculates the carry           
            curr.val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10    

            # assign the next pointer a ListNode if we have more values to add
            curr.next = ListNode() if (curr1.next or carry) else None
            
            # iterate pointers
            curr, curr1 = curr.next, curr1.next

        while curr2:
            # mod 10 calculates remainder
            # // 10 calculates the carry           
            curr.val = (curr2.val + carry) % 10
            carry = (curr2.val + carry) // 10    

            # assign the next pointer a ListNode if we have more values to add
            curr.next = ListNode() if (curr2.next or carry) else None
            
            # iterate pointers
            curr, curr2 = curr.next, curr2.next
        
        # if carry is left over assign the value to the last one
        if carry:
            curr.val = carry
        
        # return ref to the head of the result list
        return head

        """
        Inefficient 2 pass method
        """
        # curr1, curr2 = l1, l2
        # sum_ = 0
        # mult = 1
        # carry = 0
        # while curr1 and curr2:
        #     sum_ += ((curr1.val + curr2.val + carry) % 10) * mult 
        #     carry = (curr1.val + curr2.val + carry) // 10

        #     mult *= 10
        #     curr1 = curr1.next
        #     curr2 = curr2.next
        
        # while curr1:
        #     sum_ += ((curr1.val + carry) % 10) * mult 
        #     carry = (curr1.val + carry) // 10

        #     mult *= 10
        #     curr1 = curr1.next

        # while curr2:
        #     sum_ += ((curr2.val + carry) % 10) * mult 
        #     carry = (curr2.val + carry) // 10

        #     mult *= 10
        #     curr2 = curr2.next

        # sum_ += carry * mult
        # # now we have accurate sum
        # sum_ = str(sum_)[::-1]
        # head = curr = ListNode()
        # for i, c in enumerate(sum_):
        #     curr.val = int(c)
        #     if i < len(sum_) - 1:
        #         curr.next = ListNode()
        #     curr = curr.next
        # return head