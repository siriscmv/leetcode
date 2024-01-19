from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans, s, hp = 0, 0, []

        nums = list(zip(nums1, nums2))
        nums.sort(key=lambda x: x[1], reverse=True)

        for a, b in nums:
            if len(hp) == k: s -= heappop(hp)
            heappush(hp, a)
            s += a

            if len(hp) == k: ans = max(ans, s * b)

        return ans
