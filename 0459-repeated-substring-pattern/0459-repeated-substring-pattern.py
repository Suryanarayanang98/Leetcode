class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)<1:
            return True
        substr = ""
        for i in range(len(s)):
            substr += s[i]
            # sdash = "".join([substr for i in range(len(s)/(len(substr)))])
            if len(s)//(len(substr)) * substr == s and len(s) != len(substr):
                return True
        return False
