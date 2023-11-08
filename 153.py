class Solution:
    def findMin(self, nums: list[int]) -> int:
        # idea
        '''
        two pointers l, r = 0, max(nums) - 1
        # find a point m = (l + r)//2 where the left element is larger
        # and the right element is bigger
        # that point is the minimum
        
        perform binary search to find that m
        '''
        l, r = 0, len(nums) - 1
        
        # first element contains the most recently rotated element
        # everything to the left of the min val will be >= this first el
        # everything to the right will be < the first el
        
        min_el = nums[0]
        while l<=r:
            m = (l + r) // 2

            #
            if nums[m] >= nums[0]:
                # we are still in the 'first half' of the array
                # so we should move out of into the second sorted half
                l = m + 1
            else:
                # we're in the second sorted half
                # now we need to the get the left most edge of it
                # we can keep edging our right pointer to the left
                r = m - 1
                min_el = min(min_el, nums[m])

        return min_el