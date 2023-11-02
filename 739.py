class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # fill with 0 as default values
        to_return = [0] * len(temperatures)
        
        # contains a backlog of seen temperatures, 
        # will only pop off an element if we encounter a greater element than the top
        temp_stack = [] 

        # iterate over the list once
        for i, temp in enumerate(temperatures):
            # first checks stack is non empty
            # if stack is empty skips and appends new value
            # continues through while loop until 
            # we encounter a value in the stack that is >= than the current value
            while temp_stack and temp > temp_stack[-1][0]:
                # in to return list, replace the default 0 as the difference between the two indices
                to_return[temp_stack[-1][1]] = i - temp_stack[-1][1]
                
                # pop the last element off of the stack
                temp_stack.pop()
            
            # append current value, so that we can determine its correct value in future iterations
            temp_stack.append((temp, i))
        
        return to_return