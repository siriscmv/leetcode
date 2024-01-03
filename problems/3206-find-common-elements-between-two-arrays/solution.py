from collections import defaultdict

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = defaultdict(int), defaultdict(int)

        for num in nums1: c1[num] += 1
        for num in nums2: c2[num] += 1

        i, j = 0, 0
        for num in nums1: 
          if c2[num] >= 1: i += 1
        for num in nums2:
          if c1[num] >= 1: j += 1
        
        return [i, j]
