class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # k = 0, i believe this was a mistake in the constraints
        # but just a safety check. if the window size is 0, each element is of course a duplicate of itself
        # but i and j are not distinct
        if k == 0:
            return False
        
        # keeps track of the elements seen in a window of size k
        window = set()
        
        # keeps track of left edge of the window
        l = 0

        # r keeps track of the right edge of the window
        for r, _ in enumerate(nums):

            # our window is too big, so we can remove the left most element and actually increment the pointer to the leftmost element as well
            if r - l > k:
                window.remove(nums[l])
                l += 1

            # checks if the current number has been seen before, if so return True
            if nums[r] in window:
                return True
            
            # add the current number to the window
            window.add(nums[r])

        # if we never returned true, we don't have duplicates within the window
        return False