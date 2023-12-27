class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(0, l-1):
            t = target - numbers[i]
            if numbers[l-1] < t: continue
            elif numbers[l-1] == t: return [i+1, l]

            for j in range(i+1, l):
                if numbers[j] < t: continue
                elif numbers[j] == t: return [i+1, j+1]
                else: break
        
