class Solution:
    def removeDuplicates_first_try(self, nums: List[int]) -> int:
        # index 1, and last index
        l, r = 0, 1
        
        # iterate for each unique num
        for _ in range(len(set(nums)) - 1):
            # move right pointer until we find a new value
            while r < len(nums) -1 and nums[r] == nums[l]:
                r += 1
            
            # new value found, so update list
            nums[l + 1] = nums[r]

            # increment left
            l += 1

        
        return l + 1
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # start at one, since there is at least 1 unique element
        # everytime this is incremented, we have encountered a unique value
        # so, this will be our return value as well as our pointer to place new values

        # r scans through the array to find new values to place in the array determined by l
        for r in range(1, len(nums)):
            # if adjacent values are different, we have encountered a new value
            # so, we can update our list
            if nums[r] != nums[r-1]:
                nums[l] = nums[r] # update list
                
                # update our left pointer
                l += 1

        return l  