class Solution:
    def minTimeToType(self, word: str) -> int:
        t, curr = 0, ord('a')
        for char in word:
            c = ord(char)
            diff = abs(curr - c)
            diff = min(diff, abs(abs(diff)-26))
            t += diff + 1
            curr = c
        return t
