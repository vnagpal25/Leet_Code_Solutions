class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2
            guess_ = guess(m)
            if guess_ == -1:
                r = m - 1
            elif guess_ == 1:
                l = m + 1
            else:
                return m