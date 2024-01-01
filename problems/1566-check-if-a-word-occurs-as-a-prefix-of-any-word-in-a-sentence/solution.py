class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w, l1, l2, prev = 1, len(sentence), len(searchWord), ' '
        for i, ch in enumerate(sentence):
            if ch == " ": 
                w += 1
                prev = ch
                continue
            if prev != " ": 
                prev = ch
                continue
            prev = ch
            j=0
            while i+j<l1 and j<l2 and sentence[i+j] == searchWord[j]: j += 1
            if j == l2: return w
        return -1
