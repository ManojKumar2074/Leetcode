class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if  n == 0:
            return 0

        x_str = ""
        sum_digits = 0

        for char in str(n):
            if char != '0':
                x_str += char               
                sum_digits += int(char)
        
        if x_str:
            x = int(x_str) 
        else:
            x = 0
            
        return x * sum_digits

                