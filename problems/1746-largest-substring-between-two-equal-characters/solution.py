class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indices = {}
        for i, char in enumerate(s):
            if char in indices: indices[char][1] = i
            else: indices[char] = [i, i]
        return max(map(lambda i: i[1]-i[0]-1, indices.values()))
        
