class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # TRANSPOSE MATRIX
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j >= i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # REVERSE ROWS
        for i in matrix:
            i.reverse()

        

        

        