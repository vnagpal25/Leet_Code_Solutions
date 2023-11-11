"""
Solution:
keep track of a sliding window across the string with a hashmap of all seen values

use the hashmap to determine the most frequently occuring element

replacements need to make the string homogenous is : length of window (j - i + 1) - count of most frequently occuring element

this value must be less than or equal to k to be a valid substring for the problem

at each iteration make the string valid by shifting the left pointer as needed using the while loop

recalculate the max length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = k

        letter_counts = {}
        
        i = 0
        max_freq = 0
        for j in range(len(s)):
            letter_counts[s[j]] = letter_counts.get(s[j], 0) + 1

            # new character is the only one that has the chance of becoming new highest occuring character
            max_freq = max(max_freq, letter_counts[s[j]])

            # condition stated earlier in the code
            # shift left pointer
            # don't need to decrement max_freq because our solution only cares about substring with high values of 
            # max_freq. 
            # AKA if we saw a higher value already, updating it to be smaller because we are shifting the left pointer is not necessary because the length of the smaller substring will not be larger than a previously calculated max_len 
            while (j - i + 1) - max_freq > k:
                letter_counts[s[i]] -= 1
                i += 1
            
            max_len = max(j-i+1, max_len)

        return max_len

