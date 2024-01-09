class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1

        while l <= r:
            mid = (l+r) // 2
            cell = matrix[mid // n][mid % n]
            if target == cell: return True
            if target > cell: l = mid + 1
            else: r = mid - 1
        
        return False
