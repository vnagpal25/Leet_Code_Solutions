class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # initialize need matrix
        # the (i, j) entry of this matrix contains the minimum amount of candies need to survive the square
        min_health_needed = [[0 for i in range(n)] for j in range(m)]

        # how much we need to get to the last square
        
        # if there is a non-negative number in the last square, we only need 1 candy going in
        # however, if it is negative, we need at least (1 - penalty) going in to endure that penalty and survive
        min_health_needed[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # fill in last column, going from the bottom up
        # utilizing same logic as before, if the haunted house square has more than what we need for the next square, we will only need 1    going into that square
        # other wise we will need (min_needed for next square - penalty) to endure this penalty
        for i in range(m - 2, -1, -1):
            min_health_needed[i][-1] = max(1, min_health_needed[i+1][-1] - dungeon[i][-1])

        # fill in the last row, going from right to left
        # utilizing the same logic as before
        for i in range(n - 2, -1, -1):
            min_health_needed[-1][i] = max(1, min_health_needed[-1][i+1] - dungeon[-1][i])

        # fill out the rows from top to bottom
        for i in range(m - 2, -1, -1):
            # fill out the columns from right to left
            for j in range(n - 2, -1, -1):
                # only care about the minimum cost of one path, because this ensures optimality
                # so we will always choose the path that requires less candy
                min_needed_to_progress = min(min_health_needed[i+1][j], min_health_needed[i][j+1])

                # same logic as before
                # if the square has more than what we need for one of the next squares, we only need 1 going in
                # otherwise we need (min_needed for next square - penalty) to endure this penalty
                min_health_needed[i][j] = max(1, min_needed_to_progress - dungeon[i][j])

        # once we have filled out the need matrix, we can just print the first square.
        # this first element is the minimum amount of candies needed to walk through the entire maze and exit with at least 1 candy remaining
        return min_health_needed[0][0]
