class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for r in rows:
            for j in range(col):
                matrix[r][j] = 0

        for c in cols:
            for i in range(row):
                matrix[i][c] = 0