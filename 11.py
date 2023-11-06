class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = -1
        while i < j:
            # current area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[j] < height[i]:
                # right column is shorter
                # this means that varying i will not accomplish anything as the area will always be smaller than the current area
                # the reason for this is two-fold:
                # the width will always decrease
                # the height will always be less than or equal to the current height
                # so we can skip those and just consider a seperate j
                j -= 1
            elif height[i] < height[j]:
                i += 1 # similar reasoning
            else:
                # if the heights are the same
                # let's increment both pointers
                # the area will always be smaller if we consider incrementing/decrementing just one at a time
                i+=1
                j-=1
        return max_area
