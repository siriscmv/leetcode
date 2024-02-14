class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a, b, l = [], [], len(nums) // 2

        for num in nums:
            if num > 0: a.append(num)
            else: b.append(num)

        for k in range(l):
            nums[2*k] = a[k]
            nums[2*k+1] = b[k]
        return nums       
