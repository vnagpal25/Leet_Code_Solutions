class Solution:
    def get_pivot_element(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        min_el = [nums[0], 0]
        update_min_el = lambda current_min_el, new_el: new_el if new_el[0] < current_min_el[0] else current_min_el
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[0]:
                # in the first half of the array, need to go to the second
                l = m + 1
            else:
                # in the second half of the array, so need to move to its leftmost edge
                # Use the lambda function to attempt to update min_el
                min_el = update_min_el(min_el, (nums[m], m))
                r = m - 1

        return min_el[1]

    def search(self, nums: list[int], target: int) -> int:
        # find pivot element
        pivot = self.get_pivot_element(nums)

        # converts i prime to i
        i_prime_0 = len(nums) - pivot
        i_prime_to_i = lambda i_prime: i_prime - i_prime_0 if i_prime >= i_prime_0 else i_prime + pivot

        # based on pivot do binary search
        l_prime, r_prime = 0, len(nums) - 1
        while l_prime <= r_prime:
            m_prime = (l_prime + r_prime) // 2
            m = i_prime_to_i(m_prime)

            if target < nums[m]:
                r_prime = m_prime - 1
            elif target > nums[m]:
                l_prime = m_prime + 1
            else:
                return m
        
        return -1