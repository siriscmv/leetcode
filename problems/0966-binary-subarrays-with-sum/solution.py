class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans, sums = 0, deque()
        curr, l, target = 0, len(nums), goal

        for n in nums:
            sums.append(curr + n)
            curr += n
        
        for _ in range(l):
            a = bisect.bisect_left(sums, target)
            b = bisect.bisect_right(sums, target)

            ans += b - a
            target = goal + sums.popleft()
        
        return ans
