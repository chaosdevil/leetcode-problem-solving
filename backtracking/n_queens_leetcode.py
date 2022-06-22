from time import time
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # construct board
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        
        def is_valid(board, r, c):
            for i in range(len(board)):
                for j in range(c):
                    # check cell and diagonal directions
                    if board[i][j] == 'Q' and (r + j == c + i or r + c == i + j or r == i):
                        return False
            return True

        def get_string(board):
            res = []
            for i in range(n):
                s = "".join(board[i])
                res.append(s)
            return res
        
        def backtrack(col):
            if col == n:
                # construct
                result.append(get_string(board))
                return 
            
            for row in range(n):
                # check if the cell is valid
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(col+1)
                    board[row][col] = '.'
                
        backtrack(0)
        
        return result

    def solveNQueensV2(self, n: int) -> List[List[str]]:
        # construct initial board
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        result = []
        self.dfs(board, 0, result)
        
        return result

    def dfs(self, board, col, result):
        if col == len(board):
            result.append(self.construct(board))
            return
        
        for i in range(len(board)):
            if self.validate(board, i, col):
                board[i][col] = 'Q'
                self.dfs(board, col+1, result)
                board[i][col] = '.'
                
    def validate(self, board, x, y):
        for i in range(len(board)):
            for j in range(y):
                if board[i][j] == 'Q' and (x + j == y + i or x + y == i + j or x == i):
                    return False
        return True
    
    def construct(self, board):
        res = []
        for i in range(len(board)):
            s = "".join(board[i])
            res.append(s)
        return res

    def solveNQueensV3(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set()
        negDiag = set()
        
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                
                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                col.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                board[r][c] = "."
        
        backtrack(0)
        
        return res


if __name__ == "__main__":

    n = 9

    solution = Solution()

    start = time()
    print(solution.solveNQueens(n))
    print(f"Time elapsed : {(time() - start) * 1000}")

    start = time()
    print(solution.solveNQueensV3(n))
    print(f"Time elapsed : {(time() - start) * 1000}")