class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt, prev = 0, ''
        for char in s:
            if char.isalpha():
                if prev == " ": cnt = 1
                else: cnt += 1
            prev = char
        return cnt
