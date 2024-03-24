class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            ix = bisect_left(numbers, target - numbers[i])
            if ix < n and numbers[i] + numbers[ix] == target: 
                if numbers[i] != numbers[ix]: return [i+1, ix+1]
                return [i+1, ix+2]
