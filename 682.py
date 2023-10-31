class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for el in operations:
            if el == 'D':
                stack.append(stack[-1] * 2)
            elif el =='+':
                stack.append(stack[-1] + stack[-2])
            elif el == 'C':
                stack.pop()
            else: # int
                stack.append(int(el))

        return sum(stack)
            