class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren in s:
            # append matching parentheses
            if paren == '[':
                stack.append(']')
            elif paren == '{':
                stack.append('}')
            elif paren == '(':
                stack.append(')')
            # check if the corresponding parentheses matches the last added paren
            else:
                try:
                    if stack.pop() != paren:
                        return False
                except:
                    return False

        return not stack # if stack still has a parenthesis in it, return False