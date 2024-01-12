class Solution:
    trib = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        for _ in range(len(self.trib), n+1): self.trib.append(sum(self.trib[-3:]))
        return self.trib[n]   
