class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        
        # sort the array for efficient checking, O(nlogn)
        nums.sort()

        # outer for loop is O(n), inner while loop is also O(n) in the worst case
        # so this portion of the algorithm is O(n^2)
        for i, num in enumerate(nums):
            # duplicate element will return a duplicate solution, so continue
            if i > 0 and nums[i - 1] == num:
                continue

            start, end = i + 1, len(nums) -1

            while start < end:
                # compute the sum
                sum_ = num + nums[start] + nums[end]
                
                # sum is too small, shift left pointer up
                if sum_ < 0:
                    start += 1
                # sum is too large, shift right pointer down
                elif sum_ > 0:
                    end -= 1
                else:
                    # found a solution
                    res.append([num, nums[start], nums[end]])
                    
                    # shift left pointer to avoid duplicate solution
                    start += 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1

        return res  