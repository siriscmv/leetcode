class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        if len(strs) == 1: return strs[0]

        for word in strs:
            if len(word) < len(ans): ans = word
        
        if not ans: return ans

        for i in range(len(ans)-1, -1, -1):
            an = ans[:i+1]
            if not an: return ""

            if all([word.startswith(an) for word in strs]): return an

        return ""   
