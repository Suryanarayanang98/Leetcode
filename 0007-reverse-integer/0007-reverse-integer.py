class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        neg_flag = True if x<0 else False
        x = abs(x)
        while x>=1:
            y = y*10 + (x%10)
            x = x//10
        
        if neg_flag:
            y *= -1
        
        if y>2**31 - 1 or y < -2**31:
            return 0
        
        return y