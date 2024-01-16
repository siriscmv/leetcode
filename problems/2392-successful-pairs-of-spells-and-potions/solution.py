from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        l = len(potions)

        return [l - bisect_left(potions, success / spell) for spell in spells]
