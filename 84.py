class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # (index, height)
        max_area = -1

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]: 
                    i_left, h = stack.pop()
                    print(i, i_left, h)
                    max_area = max(max_area, (i - i_left) * h)
                    start = i_left
            stack.append((start, height))

        for i_l, h in stack:
            max_area = max(max_area, (i - i_l + 1) * h)
        return max_area