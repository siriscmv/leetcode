class Solution:
    def trap(self, height: List[int]) -> int:
      lr, rl = [], []

      m = 0
      for h in height:
        lr.append(m)
        m = max(m, h)
      
      m = 0
      for h in height[::-1]:
        rl.append(m)
        m = max(m, h)
      rl = rl[::-1]

      ans = 0
      for i, h in enumerate(height):
        wall = min(lr[i], rl[i])
        ans += max(0, wall - height[i])
      return ans
