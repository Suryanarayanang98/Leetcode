class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c_prf = ""
        flag = True
        iter_count = 0
        while flag:
            letters =[]
            for s in strs:
                if len(s) == 0:
                    return ""
                if iter_count < len(s):
                    letters.append(s[iter_count])
                if iter_count == len(s) - 1:
                    flag = False
            
            if len(set(letters)) == 1:
                c_prf += letters[0]
            else:
                flag = False
            iter_count += 1
        return c_prf

            