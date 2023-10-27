class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """We can partition the array into 3 chunks at each step:
            left_prefix_sum, current_element, right_suffix_sum
            We can calculate left_prefix_sum just by iterating in the rightwards direction and incrementing by the current element
            We can calculate right_suffix_sum by subtracting (left_prefix_sum + current_element) from the total_sum """
        
        # calculate total sum of elements
        total_sum = sum(nums) # linear time

        left_prefix_sum = 0 # will contain sum of all previous elements
        for i, num in enumerate(nums):
            # right_suffix_sum = total_sum - left_prefix_sum - num # calculate right suffix sum 
            # if left_prefix_sum == right_suffix_sum:
            #     return i # reached pivot index
            if left_prefix_sum == 0.5 * (total_sum - num): # this formula is equivalent to the commented out calculation, but uses less memory
                return i
            left_prefix_sum+=num # increment prefix
        
        return -1