class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:min(len(haystack),i+len(needle))] == needle:
                return i
        return -1