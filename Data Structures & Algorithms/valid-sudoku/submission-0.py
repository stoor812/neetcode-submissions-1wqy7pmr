class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check Each Row contains no duplicates
        for i in range(len(board)):
            rowSeen = set()
            for j in range (len(board[i])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rowSeen:
                    return False
                else:
                    rowSeen.add(board[i][j])
        
        # Check Each Column contains no duplicates
        for i in range(len(board)):
            colSeen = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in colSeen:
                    return False
                else:
                    colSeen.add(board[j][i])
        
        # Check Each Box contains no duplicates
        for square in range(9):
            boxSeen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in boxSeen:
                        return False
                    else:
                        boxSeen.add(board[row][col])

        return True
        