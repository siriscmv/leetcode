class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i, j, l1, l2 = 0, 0, len(word1), len(word2)

        while i<l1 or j<l2:
            if i<l1: ans.append(word1[i])
            if j<l2: ans.append(word2[j])
            i += 1
            j += 1
        
        return "".join(ans)
