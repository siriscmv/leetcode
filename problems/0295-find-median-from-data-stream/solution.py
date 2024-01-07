from bisect import bisect_right

class MedianFinder:

    def __init__(self):
      self.nums = []

    def addNum(self, num: int) -> None:
      i = bisect_right(self.nums, num)
      if i == len(self.nums): self.nums.append(num)
      else: self.nums.insert(i, num)

    def findMedian(self) -> float:
      l = len(self.nums)
      mid = l//2
      if l%2 == 0: return (self.nums[mid-1] + self.nums[mid]) / 2
      else: return self.nums[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
