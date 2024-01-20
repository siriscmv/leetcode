class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans, stack = 0, []
        arr.insert(0, -inf)
        arr.append(-inf)

        for i, n in enumerate(arr):
            while stack and n < arr[stack[-1]]:
                mid = stack.pop()
                left = mid - stack[-1]
                right = i - mid
                ans += arr[mid] * left * right

            stack.append(i)

        return ans % (10 ** 9 + 7)
