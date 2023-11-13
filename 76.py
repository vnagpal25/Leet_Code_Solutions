from collections import Counter
class Solution:    
    def minWindow(self, s: str, t: str) -> str:
        # permutations of the same string have the same hashmap
        # in this case the perms hashmap needs to be a subset of the substring's hashmap
        perm_ = Counter(t)
        
        # efficient, no need to check anymore
        if Counter(s[: len(t)]) == perm_: return s[:len(t)]                

        # have is the number of letter conditions that we have met
        # need is the number of letter conditions that we have to meet
        have = 0
        need = len(perm_)

        # keeps track of the indices of minimum substring
        res = [-1, -1]
        # keeps track of minimum length substring
        min_len = float('infinity')

        # window contains the letter counts for the letters between i and j inclusive
        window = {}
        i = 0

        # iterates right pointer over string
        for j in range(len(s)):
            # update our hashmap
            window[s[j]] = window.get(s[j], 0) + 1
            
            # checks if we've met a letter condition
            if s[j] in perm_ and window[s[j]] == perm_[s[j]]:
                have += 1

            # while we have enough letters, keep shifting left pointer over
            while have == need:
                # only updates result variables if the new substring is smaller
                if j - i + 1 < min_len:
                    res = [i, j]
                    min_len = j - i + 1

                # removes left most element from the window
                window[s[i]] -= 1
                
                # checks if we have violated a condition
                if s[i] in perm_ and window[s[i]] < perm_[s[i]]:
                    have -= 1
                i += 1
        
        # returns the new substring only if the condition was ever met
        return s[res[0] : res[1] + 1] if res != [-1, -1] else ""
