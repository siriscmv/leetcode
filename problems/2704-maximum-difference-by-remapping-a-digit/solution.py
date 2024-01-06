class Solution:
    def minMaxDifference(self, num: int) -> int:
        n = str(num)
        maxx = n.replace(next((nn for nn in n if nn != '9'), '0'), '9')
        minn = n.replace(n[0], '0')

        return int(maxx) - int(minn)
