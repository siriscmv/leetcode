class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m, i, ans = -1, len(arr)-1, [0] * len(arr)
        while i >= 0:
            ans[i] = m
            m = max(m, arr[i])
            i -= 1
        return ans
