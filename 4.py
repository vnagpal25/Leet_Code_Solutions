class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        """
        Idea here is to determine (left and right) partitions of the array without actually merging the arrays
        We can exploit the sorted nature of both arrays
        the left partition of the merged array will include some number of elements of the left of both arrays
        this will be floor(total els / 2)


        We start off by assuming that exactly half of the smaller array is included in the left partition
        if this is not the case, we either decrement the smaller arrays contribution or increment it
        we repeat until we have reached a valid partition (left of A <= right of B and left of B <= right of A)
        
        if left of A > right of B, then A is overcontributing so we need to decrement A
        if left of B > right of A, then B is overcontributing so we need to increment A

        """
        # want to perform binary search on the shorter list
        if len(B) < len(A):
            A, B = B, A

        total_el = len(A) + len(B)
        half = total_el // 2 # left partition size
        l, r = 0, len(A) - 1

        # there is a median, so we can just return out the median which breaks the loop
        while True:
            m_a = (l + r)//2
            m_b = half - m_a - 2 # m_b = (number of els in b's partition) - 1 = (half - len of A's partition) - 1 = (half - (m_a + 1)) - 1= half - m_a - 2
            

            # infinities handle edge cases
            
            # if the left partition is entirely in one of the arrays. so -infinity is always smaller than Bright or Aright
            Aleft = A[m_a] if m_a >= 0 else float('-infinity')
            Bleft = B[m_b] if m_b >= 0 else float('-infinity')

            # if the left partition spans the entirety of one array, then there is no corresponding right element
            # so A left or B left are always smaller than infinity 
            Aright =  A[m_a + 1] if (m_a + 1) < len(A) else float('infinity')
            Bright = B[m_b + 1] if (m_b + 1) < len(B) else float('infinity')

            # correct partition found
            if Aleft <= Bright and Bleft <= Aright:
                # odd number of elements
                if total_el % 2:
                    return min(Bright, Aright)
                # even number of elements
                else:
                    return 0.5 * (max(Aleft, Bleft) + min(Aright, Bright))
            # read documentation above from binary search incrementing/decrementing
            elif Aleft > Bright:
                r = m_a - 1
            else:
                l = m_a + 1