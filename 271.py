class Solution:
    def encode(self, strs:list[str]) -> str:
        # write your code here
        res =""
        for s in strs:
            res+=(f'{len(s)}%{s}')
        
        return res


    def decode(self, str:str) -> list[str]:
        # contains list of decoded strings to return
        res = []

        # points to location in string
        i = 0

        # iterate over entire string
        while i < len(str):
            # start pointer j at i
            j = i

            # '%' is the delimeter, everything before it is the length of the string
            while str[j] != '%':
                j += 1
            
            length = int(str[i:j])
            
            # extract string and append it
            res.append(str[j + 1 : j + 1 + length])

            # skip to next string or end of string
            i = j + length + 1 
        
        return res
