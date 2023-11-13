from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap of the permutation string
        perm_ = Counter(s1)

        # length of the permutation
        perm_length = len(s1)

        # hashmap of first substring that is the same size as the permutation string
        window = Counter(s2[:perm_length])

        # sliding window technique
        # if hashmap is good, return True
        # if not, drop left element and add the next right element
        for i in range(1, len(s2) - perm_length + 1):
            # match found, return True
            if window == perm_:
                return True
            
            # drop left
            window[s2[i - 1]] -= 1
            
            # add new right
            window[s2[i + perm_length -1 ]] = window.get(s2[i + perm_length -1 ], 0) + 1

        # in case the permutation was the final possible substring and we didn't have a chance to check it
        return window == perm_
        