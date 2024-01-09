class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        l, ans = len(digits), set()
        for i, c in enumerate(digits):
            if c % 2 != 0: continue
            for j, a in enumerate(digits):
                if i == j or a == 0: continue
                for k, b in enumerate(digits):
                    if k == i or k == j: continue
                    ans.add(a*100 + b*10 + c)

        return sorted(ans) 
