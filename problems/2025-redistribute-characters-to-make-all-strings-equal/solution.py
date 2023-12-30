class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l, counts = len(words), {}
        for word in words:
            for char in word:
                counts[char] = counts.get(char, 0) + 1
        for val in counts.values():
            if val % l != 0: return False
        return True
