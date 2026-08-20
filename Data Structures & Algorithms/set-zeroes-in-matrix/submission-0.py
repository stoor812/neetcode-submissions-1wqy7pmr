class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        # FIND ZEROS
        for row in range(len(matrix)):
            for val in range(len(matrix[row])):
                if matrix[row][val] == 0:
                    rows.add(row)
                    cols.add(val)

        # UPDATE MATRIX ROWS
        for row in range(len(matrix)):
            for val in range(len(matrix[row])):
                if row in rows or val in cols:
                    matrix[row][val] = 0
