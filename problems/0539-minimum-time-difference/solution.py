class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            timePoints[i] = int(time[:2]) * 60 + int(time[3:])

        timePoints.sort()
        timePoints.append(timePoints[0] + 24 * 60)
        ans = float("inf")
        for i in range(len(timePoints) - 1):
            diff = min(
                abs(timePoints[i + 1] - timePoints[i]),
                24 * 60 - abs(timePoints[i + 1] - timePoints[i]),
            )
            if diff < ans:
                ans = diff
        return ans


