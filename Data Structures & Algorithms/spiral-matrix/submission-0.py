class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1    
        top = 0
        bottom = len(matrix) - 1
        spiral = []

        while left <= right and top <= bottom:

            if left <= right and top <= bottom:
                # LEFT TO RIGHT
                for i in range(left, right + 1):
                    spiral.append(matrix[top][i])
                top += 1
            if left <= right and top <= bottom:
                # TOP TO BOTTOM
                for i in range(top, bottom + 1):
                    spiral.append(matrix[i][right])
                right -= 1
            if left <= right and top <= bottom:
                # RIGHT TO LEFT
                for i in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][i])
                bottom -= 1
            if left <= right and top <= bottom:
                # BOTTOM TO TOP
                for i in range(bottom, top - 1, -1):
                    spiral.append(matrix[i][left])
                left += 1

        return spiral
