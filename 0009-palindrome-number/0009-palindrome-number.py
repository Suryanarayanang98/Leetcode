class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev_num = 0
        x_copy = x
        iter = 0 
        while x_copy>0:
            rem = x_copy % 10
            x_copy = x_copy// 10
            rev_num += rem*10**(len(str(x)) - iter - 1)
            iter += 1

        if rev_num == x:
            return True
        return False

