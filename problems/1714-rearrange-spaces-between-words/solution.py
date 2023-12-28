class Solution:
    def reorderSpaces(self, text: str) -> str:
        i, j, l = 0, 0, len(text)
        spaces, words = 0, []

        while i < l:
            if text[i] == ' ': 
                spaces += 1
                i += 1
            else:
                j = i + 1
                while j < l and text[j] != ' ': j += 1
                if j < l and text[j] == ' ': spaces += 1
                words.append(text[i:j])
                i = j+1
        
        w = len(words)
        if w == 1: return words[0] + " " * spaces
        return (" " * (spaces // (w-1))).join(words) + " " * (spaces % (w-1))
