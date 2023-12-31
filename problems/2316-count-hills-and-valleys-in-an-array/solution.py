class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n, prev = [], None

        for num in nums:
            if num != prev:
                n.append(num)
                prev = num

        h, v = 0, 0
        for i in range(1, len(n)-1):
            l, c, r= n[i-1], n[i], n[i+1]
            if c>l and c>r: h += 1
            elif c<l and c<r: v += 1
        
        return h+v
