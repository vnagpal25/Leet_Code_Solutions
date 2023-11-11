class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 # i represents the left edge of the sliding window
        sum_ = nums[0] # initial sum is the first element
        
        # this is an edge case, if the first element is enough, that is the minimum
        # so just return
        if sum_ >= target:
            return 1
        
        # default value
        min_size = float("infinity") 
        
        # start at the second element
        for j in range(1, len(nums)):
            # compute new sum
            sum_ += nums[j] 
           
            # while the current window contains a large enough sum
            # decrement the window size and the sum and keep updating min_size
            while sum_ >= target:
                # new min size
                min_size = min(min_size, j - i + 1)
                
                # decrement sum and update i
                sum_ -= nums[i]
                i += 1
            
        # if the sum was never enough, min size was never updated so return infinity 
        return min_size if min_size < float("infinity") else 0