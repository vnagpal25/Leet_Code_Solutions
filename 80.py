class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        The goal here is to use two pointers
        We start them both(l, r) at index 1
        l: represents the current unique element, the final value will be the number of allowed elements in the final list
        r: scans through the list to update the values of nums[l]

        We update values at nums[l] and increment l based on two conditions:
        Condition 1 - We encountered a new value that hasn't been seen before (nums[r] != nums[r - 1]). 
        
        Condition 2 - 
            We encountered a value that was seen last time l was updated
            nums[r] == nums[l - 1] 
            
            and
            
            This is not the third time we are seeing this value
            nums[l - 1] != nums[l - 2]
            or this value is repeated version of the first element of the list and l = 1
            l < 2
        '''
        l = 1

        for r in range(1, len(nums)):
            # encountered second unique value
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]               
                l += 1
            elif nums[r] == nums[l-1] and (l < 2 or nums[l-1] != nums[l - 2]):
                nums[l] = nums[r]
                l += 1                
    
        return l