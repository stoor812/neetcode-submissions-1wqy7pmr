class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        colZero = False
        
        # IDENTIFY ZEROS
        for row in range(len(matrix)):
            for val in range(len(matrix[row])):
                if matrix[row][val] == 0:
                    matrix[row][0] = 0
                    matrix[0][val] = 0
                    
                    if row == 0:
                        rowZero = True
                    if val == 0:
                        colZero = True

        # UPDATE MATRIX ROWS
        for row in range(len(matrix)):
            for val in range(len(matrix[row])):
                if row > 0 and val > 0:
                    if matrix[row][0] == 0 or matrix[0][val] == 0:
                        matrix[row][val] = 0
        
        # UPDATE ZERO ROW / COL 
        if rowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if colZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        