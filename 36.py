import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # check row conditions
        # map row to a set of numbers
        rows = collections.defaultdict(set)
        
        # check column conditions
        # map col to a set of numbers
        cols = collections.defaultdict(set)
        
        # check square conditions
        # map (r // 3, c // 3) to a set of numbers
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                # we have already encountered such a number before
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True