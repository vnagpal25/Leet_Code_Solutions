# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        min_bad = n
        while l <= r:
            m = (l + r) // 2

            if isBadVersion(m):
                # everything after this is bad, so lets search before
                r = m -1
                min_bad = min(min_bad, m)
            else:
                l = m + 1

        return min_bad
