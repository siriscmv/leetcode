class Solution:
    def strStr(self, haystack, needle):
        a, b = len(needle), len(haystack)

        if a > b: return -1
        for i in range(b - a + 1):
            if haystack[i: i+a] == needle: return i
        return -1
