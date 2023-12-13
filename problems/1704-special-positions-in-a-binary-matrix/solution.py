class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        count = 0

        for r, line in enumerate(mat):
            for c, val in enumerate(line):
                if val == 1:
                    rows[r] += 1
                    cols[c] += 1

        for r, line in enumerate(mat):
            for c, val in enumerate(line):
                if val == 1 and rows[r] == 1 and cols[c] == 1:
                    count += 1

        return count
