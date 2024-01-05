class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      cars, ans = list(zip(position, speed)), 0
      cars.sort()
      while len(cars) > 1:
        a, b = cars[-2], cars[-1]
        t1, t2 = (target-a[0])/a[1], (target-b[0])/b[1]
        if t2 < t1: 
          ans += 1
          del cars[-1]
        else: del cars[-2]

      return 1 + ans
