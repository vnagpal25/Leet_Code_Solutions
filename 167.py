class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        
        # the theory here is to not checking every corresponding pair
        # but to exploit the sorted nature of the list
        # we can use a two pointers approach
        # if the sum of a left el and a right el is too big, we can shift the right pointer so that the sum is smaller
        # likewise is the sum is smaller we can shift the left pointer to the right
        # when the sum is correct, return the results
        while i < j:
            sum_ = numbers[i] + numbers[j]

            if sum_ < target:
                # under shooting sum so we need to make it bigger
                # shift left pointer
                i += 1
            elif sum_ > target:
                # over shooting sum so we need to make it smaller
                # shift right pointer
                j -= 1
            else:
                return [i + 1, j + 1]