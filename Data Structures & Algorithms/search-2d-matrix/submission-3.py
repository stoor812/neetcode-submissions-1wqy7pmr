class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows*cols - 1

        while left <= right:
            middle = (left + right) // 2
            # Convert to 2D MATRIX
            m1 = middle // cols
            m2 = middle % cols
            if matrix[m1][m2] < target:
                # Target is less than search left
                left = middle + 1
            elif matrix[m1][m2] > target:
                # Target is greater than search right
                right = middle - 1
            else:
                return True

        return False