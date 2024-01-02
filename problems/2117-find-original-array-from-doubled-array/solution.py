from collections import defaultdict


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        count = defaultdict(int)
        ans = []

        for num in changed:
            count[num] += 1
        for num in changed:
            if count[num] <= 0:
                continue
            double = num * 2
            if double not in count or count[double] == 0:
                return []
            ans.append(num)
            count[num] -= 1
            count[double] -= 1

        return ans

