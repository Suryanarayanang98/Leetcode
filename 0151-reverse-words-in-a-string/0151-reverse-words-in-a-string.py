class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i.strip() for i in s.strip().split() if i.strip()!=""]
        def rev(left_index):
            nonlocal s
            if left_index >= len(s) - 1:
                return
            right_val = s[-1]
            for i in range(len(s)-1,left_index-1,-1):
                if i!=left_index:
                    s[i] = s[i-1]
                else:
                    s[left_index] = right_val
            rev(left_index+1)
            return
        rev(0)
        return " ".join(s)
        



            