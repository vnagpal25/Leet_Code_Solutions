class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == '+':
                nums.append(nums.pop() + nums.pop())
            elif token == '/':
                nums.append(int(1/(nums.pop()) * nums.pop()))
            elif token == '*':
                nums.append(nums.pop() * nums.pop())                
            elif token == '-':
                nums.append(-nums.pop() + nums.pop())                
            else:
                nums.append(int(token))
        return nums[0]