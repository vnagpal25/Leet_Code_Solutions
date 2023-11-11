"""
Solution:
Sliding window approach maintains left and right pointer
# prices[r] - prices[l] determines the profit
# if this value is profit, calculate the profit and determine if it is the max profit
# if this value is loss or no gain, then we shift the left pointer all the way to the right pointer
# because this means that the right price is very low and we want to buy at that price
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i, j = 0, 1 # maintain ends of the window

        max_prof = 0 # contains the max profit
        
        # iterate through the array
        while j < len(prices):
            # no profit, so shift to buy at really low price
            if prices[j] <=  prices[i]:
                i = j
            # record the maximum profit
            else:
                max_prof = max(max_prof, prices[j] - prices[i])
            
            # shift the right pointerd
            j += 1
        # return the maximum profit
        return max_prof

