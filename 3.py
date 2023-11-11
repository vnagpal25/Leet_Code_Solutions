class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if len(s) == 0:
            return 0
        
        # left pointer of window
        i = 0

        # initialize window with first character
        window = {s[0]}
        
        # max len is at least 1
        max_len = 1
        
        # iterate from the first character
        for j in range(1, len(s)):
            

            # calculate the max length of the repeating substring
            max_len = max(max_len, j - i)
            
            # while the current character is already in the window, increment our left pointer
            # until it isn't anymore           
            while s[j] in window:

                window.remove(s[i])
                i += 1
            
            # add new character to the window
            window.add(s[j])

        return max(max_len, len(window))