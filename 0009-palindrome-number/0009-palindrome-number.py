class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        strx = str(x)
        for i in range(len(strx)//2):
            if strx[i] != strx[len(strx) - i - 1]:
                return False
        
        return True