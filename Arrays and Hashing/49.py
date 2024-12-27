from typing import *
"""https://leetcode.com/problems/group-anagrams/description/"""

# two approaches:
# sorting each string within the main for loop (m * nlogn time complexity)
# populating a table with the counts of each letter in the word (m * n time complexity)
# m is number of string, n is length of longest string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            # sort the string alphabetically
            # all anagrams will have the same sorted string

            # # # # # key = ''.join(sorted(string))

            # alternative approach, instead of sorting, we count the number of each letter
            # initialize each letter with 0 counts at beginning
            counts = [0]*26
            for ch in string:
                counts[ord(ch) - ord('a')] += 1
            # convert table to tuple which is an immutable hashable type
            key = tuple(counts)

            # we keep all anagrams in the same list as a value in the hashmap with the sorted string being the hash key
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        # return the values
        return list(anagrams.values())
