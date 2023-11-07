class Solution:
    # O(log(n)) binary search
    def search(self, nums: List[int], target: int) -> int:
        # initialize left and right pointers as ends of array
        l, r = 0, len(nums) - 1

        # l > r means whole array has been searched, so return -1
        while l <= r:
            # compute middle index
            m = (r + l) // 2
            
            # in the first half of the array
            if target < nums[m]:
                r = m - 1
            # in the second half of the array
            elif target > nums[m]:
                l = m + 1
            # is the middle element!
            elif target == nums[m]:
                return m
            
        return -1
