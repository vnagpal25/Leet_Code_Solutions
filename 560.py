class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # brute force approach
        # calculate sum for all subarrays and count how many 
        # this would be O(n^2) complexity as there are n(n+1)/2 subarrays in an array of length n

        to_ret = 0
        prefix_sums = {0:1} # maps prefix sums to counts 
        total_sum = 0

        for num in nums:
            total_sum += num

            # if we can remove a prefix that sums up to (total_sum - k), then we can create a sub array that sums to k
            """
            Consider [1, 1, 1, 1] k = 3 at i = 3
            the total sum here is 3. 3 - 3 = 0. We need to remove a subarray that sums up to zero to reach our goal
            good for us the empty prefix counts as the whole array also counts as a subarray
            now let us consider i = 4
            4-3 =1, we need to remove a prefix array that sums to 1 from this
            of course this is the first element.
            we know this because we have been keeping track of prefix sums with the hashmap 
            """
            prefix_sum_needed = total_sum - k

            to_ret += prefix_sums.get(prefix_sum_needed, 0) # all the different ways we can achieve this prefix will allow us to remove those prefixes from the total sum thus far and thus have a sum of k
            
            prefix_sums[total_sum] = prefix_sums.get(total_sum, 0) + 1
        return to_ret
