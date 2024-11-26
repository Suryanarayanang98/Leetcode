class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = -1

        for k,v in dic.items():
            if v != -1:
                return v
        return -1
