class Solution:
    def maxProduct(self, words: List[str]) -> int:
        for i, word in enumerate(words):
            words[i] = (len(word), set(word))
        words = sorted(words, key=lambda x: x[0], reverse=True)
        ans=0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                a,b = words[i], words[j]
                if not a[1].intersection(b[1]): 
                    res = a[0]*b[0]
                    if res>ans: ans=res
        return ans
