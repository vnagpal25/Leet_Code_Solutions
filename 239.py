from collections import deque 
from typing import List

"""
The idea here is to use a modified sliding window approach to calculate the maximum value
in each window of size k

We can achieve this in O(n) time complexity and O(n) space complexity

We maintain an array 'res' which contains the maximum element in each sliding window (determined by left pointer i and right pointer j)

We also maintain a deque which is monotonically decreasing
We append values to it if the last value added is >=
If the last added is smaller, then we pop off the smaller ones until we get a >= one

We also pop off the left element of the deque if it was never removed (aka it was the max of the previous window)

At the end of each window, the first element of the deque always contains the maximum value of that window. So we append to our output array.
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        max_deque = deque()

        i = 0

        # increment the right pointer continuously
        for j in range(len(nums)):
            # pop off elements that are smaller than the current element
            while max_deque and nums[max_deque[-1]] < nums[j]:
                max_deque.pop()
            
            # add the current element which is either the only element or smaller than
            # the other elements to the left of it 
            max_deque.append(j)

            # pop off the max value's index of the previous window
            if max_deque[0] < i:
                max_deque.popleft()
            
            # we have scanned an entire window we can append the first value of the deque
            # which contains the max index of that window
            # we then increment the left pointer
            if (j + 1) >= k:
                res.append(nums[max_deque[0]])
                i += 1
        
        # return the output array
        return res


