class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(map(lambda word: word.strip(), s.strip().split(' ')))
        return " ".join([w for w in words[::-1] if w])
