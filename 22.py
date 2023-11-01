class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # will only add a open paren if open < n
        # will only add a closed paren if closed < open
        # stops when open == closed == n

        stack = []
        parens = []

        # depth first search based solution
        def dfs_parens(open_paren_count, closed_paren_count):
            # no more parentheses to add
            if open_paren_count == closed_paren_count == n:
                # combine all elements in the stack appends it, and returns to continue down the n-1st node's path
                parens.append("".join(stack))
                return
            
            # explores path of adding open parens
            if open_paren_count < n:
                # appends paren to stack
                stack.append('(')

                # now solve a simpler version of the problem (keep traversing down path)
                dfs_parens(open_paren_count + 1, closed_paren_count)
                
                # we have exhausted this path now, so pop off the paren and continue
                stack.pop()
            
            # explores the path of adding closed parens
            if closed_paren_count < open_paren_count:
                # appends paren to stack
                stack.append(')')

                # now solve a simpler version of the problem (keep traversing down path)
                dfs_parens(open_paren_count, closed_paren_count  + 1)

                # exhausted possibilities, now continue and pop off the last added
                stack.pop()

                # end of function officially return
                return
        
        # start off with 0 of each parenthesis
        dfs_parens(0, 0)

        # return solution
        return parens