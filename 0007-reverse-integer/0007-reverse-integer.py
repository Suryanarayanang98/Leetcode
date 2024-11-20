class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        count = 0
        neg_flag = True if x<0 else False
        x = abs(x)
        length = len(str(x))
        while x>=1:
            rem = x%10
            y += rem*10**(length - 1 - count)
            count+=1
            x = x//10
            
        y = -y if neg_flag else y
        if y>2**31-1 and not neg_flag:
            return 0
        if y<-2**31 and neg_flag:
            # print("here")
            return 0 
        
        return y