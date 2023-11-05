class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers approach
        # checking corresponding alphanumeric characters from the left and right
        
        # first/last element
        i, j = 0, len(s) - 1

        # while they don't pass each other
        while i <= j:

            # reached non alphanumeric on left, increment and continue
            if not (s[i].isalnum()):
                i += 1
                continue

            # reached non alphanumeric on right, decrement and continue
            if not (s[j].isalnum()):
                j -= 1
                continue
            
            # both characters are alphanumeric, if they are not equal return False
            if (s[i].lower() != s[j].lower()):
                return False

            # increment/decrement
            i, j = i + 1, j - 1
        
        # return true
        return True