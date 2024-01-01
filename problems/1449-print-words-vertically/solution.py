class Solution:
    def printVertically(self, s: str) -> List[str]:
        words, ans = s.split(' '), []
        for i in range(0, max([len(w) for w in words])):
            curr = []
            for w in words:
                if i<len(w): curr.append(w[i])
                else: curr.append(' ')
            ans.append("".join(curr).rstrip(' '))
        return ans
