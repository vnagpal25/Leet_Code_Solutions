class Solution:
    
    def constructShiftTable(self, string, str_len):
        shift_table = {}
        for i, char in enumerate(string[:-1]):
            shift_table[char] = str_len - 1 - i
        return shift_table

    # only boyer moore horspool (using bad character match)
    def strStr(self, haystack: str, needle: str) -> int:
        # Boyer Moore Horspool (Bad Match Table only)
        m = len(needle)
        n = len(haystack)
        shift_table = self.constructShiftTable(needle, m)
        
        # lining up pattern with string
        i = m - 1
        while i <= n - 1:
            k = 0 # points to first character of needle from the right
            
            # loop through portion of haystack (don't go past pattern, and make sure characters match)
            while (k <= m - 1 and needle[m - 1 - k] == haystack[i - k]):
                k += 1
            if k == m: # the while loop was exited because the entire pattern found a match
                return i - m + 1
            else:
                # utilize the shift table to shift the rightmost pointer
                i += shift_table.get(haystack[i], m)
        # we've gotten to the end of the haystack and we haven't found the needle, so we return -1
        return - 1
