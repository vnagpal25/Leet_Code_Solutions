class Solution:
    # O(n) time complexity
    # O(1) space complexity because we are using 2 pointers
    # we could alternatively store a few precomputed arrays for O(n) space complexity
    # however, the time complexity would remain the same

    def trap(self, height: list[int]) -> int:
        # the amount of water a space can hold is determined by this formula
        # min(left_height, right_heights) - h[i]
        # left_height - the maximum height seen to the left of i
        # right_height - the maximum height seen to the right of i
        # h[i] - height at i
        # consider the first water square on the left:
        # the max height on the left is one, the max height on the right is 3
        # min(1, 3) = 1
        # 1 - h[i] = 1 - 0 = 1 water capacity

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        total_cap = 0
        while l < r:
            # if maxL is smaller, and maxR is only going to increase, we can compute
            # the water capacity for the l square using the above specified formula 
            if maxL < maxR:
                l += 1 # increment first, so we don't calculate cap for the 0 index
                maxL = max(maxL, height[l]) # computing the new left max
                total_cap += (maxL - height[l]) # gauranteed to be non negative
            else:
                # smaller element on the right
                # smaller element on the left
                r -= 1 # decrement first, so we don't calculate cap for the -1 index
                maxR = max(maxR, height[r]) # computing the new left max
                total_cap += (maxR - height[r]) # gauranteed to be non negative
        return total_cap
