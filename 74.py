class Solution:

    def search_list(self, row, target):
         # initialize left and right pointers as ends of array
        l, r = 0, len(row) - 1

        # l > r means whole array has been searched, so return -1
        while l <= r:
            # compute middle index
            m = (r + l) // 2
            
            # in the first half of the array
            if target < row[m]:
                r = m - 1
            # in the second half of the array
            elif target > row[m]:
                l = m + 1
            # is the middle element!
            elif target == row[m]:
                return True
            
        return False       


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        low_row_i, high_row_i = 0, m - 1

        while low_row_i <= high_row_i:
            mid_row_i = (low_row_i + high_row_i) // 2

            mid_row = matrix[mid_row_i]

            if target < mid_row[0]:
                high_row_i = mid_row_i - 1
            elif target > mid_row[n-1]:
                low_row_i = mid_row_i + 1
            else:
                # perform binary search on this single row
                return self.search_list(mid_row, target)
        return False