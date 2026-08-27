class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldCol = image[sr][sc]
        visited = set()

        def dfs(grid, row, col, visited):
            # OUT OF BOUNDS
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            
            # ALREADY SEEN / WRONG COLOR
            if (row, col) in visited or grid[row][col] != oldCol:
                return

            # MARK
            image[row][col] = color
            visited.add((row,col))

            # EXPLORE
            dfs(grid, row - 1, col, visited)
            dfs(grid, row + 1, col, visited)
            dfs(grid, row, col - 1, visited)
            dfs(grid, row, col + 1, visited)

        dfs(image, sr, sc, visited)

        return image