class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        num_windows = 0
        curr_sum = sum(arr[:k-1]) # sum first k - 1 values
        
        for j in range(len(arr) - k + 1):
            curr_sum += arr[j + k - 1] # add rightmost
            if (curr_sum/k) >= threshold: # compute mean
                num_windows +=1
            curr_sum -= arr[j] # subtract leftmost
        return num_windows