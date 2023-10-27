class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        # dimensions
        row_num, col_num = len(matrix), len(matrix[0])
        
        # zero array to hold prefix sums
        self.prefix_sums = [[0 for i in range(col_num)] for j in range(row_num)]
        
        # iterate over the rows
        for i, row in enumerate(matrix):
            prefix = 0 # the initial prefix for each row should be 0
            # iterate over each element in a row
            for j, element in enumerate(row):
                prefix += element # calculate the row prefix sum based on sum of prefix and current element
                
                # if this isn't the first row, then add the previous row's prefix sum to get combined sum for matrix with corners:
                # (0, 0) and (i, j)
                if i > 0:
                    self.prefix_sums[i][j] += self.prefix_sums[i-1][j]

                # also add the current row's contribution
                self.prefix_sums[i][j] += prefix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''Draw a picture to understand this better'''

        # sum of full matrix from (0, 0) to (r2, c2)
        sum_to_ret = self.prefix_sums[row2][col2] 

        # if not the first row, then subtract the previous row's prefix sum
        # we are subtracting the sum of the matrix from (0, 0) to (r1-1, c2)
        # subtracting above sum            
        if row1 > 0:
            sum_to_ret -= self.prefix_sums[row1 -1][col2]
        
        
        # if not the first column, then subtract the previous column's prefix sum
        # we are subtracting the sum of the matrix from (0, 0) to (r2, c1-1)
        # subtracting above sum
        if col1 > 0:
            sum_to_ret -= self.prefix_sums[row2][col1 -1]

        # if we have subtracted twice, add it back
        # add back the matrix from (0, 0) to (r1 - 1, c1 -1)
        if row1 > 0 and col1> 0:
            sum_to_ret += self.prefix_sums[row1-1][col1-1]
        
        return sum_to_ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)