class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = set(range(1, n+1))
        for a, b in trust: 
            if a in people: people.remove(a)
        
        if len(people) != 1: return -1
        
        c, judge = 0, list(people)[0]
        
        for a, b in trust:
            if judge == b: c += 1

        if c == n-1: return judge
        return -1
