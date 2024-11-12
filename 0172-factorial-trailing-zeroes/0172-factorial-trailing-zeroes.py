class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if n<5:
            return 0
        j=0
        s=n
        sums=0
        while not s<1:
            j=j+1
            s=n//(5**j)
            sums=sums+(s)
        return sums
            
            
        