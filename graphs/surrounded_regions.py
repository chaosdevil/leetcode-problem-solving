from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(board, row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return
                
            board[row][col] = "*"
            
            for d in directions:
                r = row + d[0]
                c = col + d[1]
                if r >= 0 and r < n:
                    if c >= 0 and c < m:
                        if board[r][c] == "O":
                            flag = dfs(board, r, c)
                                    
        # start from boundary rows
        for c in range(m):
            if board[0][c] == "O":
                dfs(board, 0, c)
            if board[n-1][c] == "O":
                dfs(board, n-1, c)
        
        # start from boundary columns
        for r in range(n):
            if board[r][0] == "O":
                dfs(board, r, 0)
            if board[r][m-1] == "O":
                dfs(board, r, m-1)
        
        for i in range(n):
            for j in range(m):
                board[i][j] = "X" if board[i][j] in ["O","X"] else "O"


if __name__ == "__main__":
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","O"],["X","O","X","X"]]

    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

    solution = Solution()
    solution.solve(board)
    print(board)