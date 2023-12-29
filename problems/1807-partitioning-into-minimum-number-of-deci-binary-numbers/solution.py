class Solution:
    def minPartitions(self, n: str) -> int:
        return self.solve(list(n))
    
    def strip(self, num):
        while len(num) >= 1 and num[0] == '0': del num[0]
        return num
    
    def solve(self, num):
        if len(num) == num.count('0'): return 0
        return 1 + self.solve([str(max(0, int(n)-1)) for n in num])

        
