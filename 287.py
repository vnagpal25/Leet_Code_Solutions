from typing_extensions import List
"""
Model this problem as a Linked List with a cycle

each number in the array will be a valid index for the array

because there are duplicate values there is a cycle (drawing a picture helps)

we want to find the index of the start of the cycle (this will be value to return)

We will use Fast and Slow pointers to first find the intersection within the cycle

We will then use another slow pointer(starting from 0) to determine their second intersection with the first slow pointer

This index will be the value to return
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # determine intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # determine second intersection (start of cycle)
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            
            if slow == fast:
                return slow