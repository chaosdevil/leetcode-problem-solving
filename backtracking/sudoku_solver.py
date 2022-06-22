import os

from ast import literal_eval
from typing import List
from time import time

class Solution:
    n = 9
    def solveSudoku(self, board: List[List[str]]):
        
        def solve(board: List[List[str]], row, col):
            if row == self.n - 1 and col == self.n:
                return True

            if col == self.n:
                row += 1
                col = 0

            if board[row][col] != '.':
                return solve(board, row, col + 1)

            for num in range(1, 10):
                if is_safe(board, row, col, num):
                    board[row][col] = str(num)

                    if solve(board, row, col + 1):
                        return True

                board[row][col] = '.'
            
        def is_safe(board, row, col, num):
            for x in range(0, 9):
                if board[row][x] == str(num):
                    return False

            for x in range(0, 9):
                if board[x][col] == str(num):
                    return False

            start_row = row - row % 3
            start_col = col - col % 3

            for i in range(3):
                for j in range(3):
                    if board[i + start_row][j + start_col] == str(num):
                        return False

            return True
       
        solve(board, 0, 0)

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    solution = Solution()
    with open(os.path.dirname(__file__) + \
            "/sudoku_solver_testcase.txt", "r") as file:
        board = literal_eval(file.readline().strip())

    start = time()
    print("Original board")
    print_board(board)
    
    solution.solveSudoku(board)

    print("\nSolved!")
    print_board(board)
    print(f"Time elapsed: {(time() - start) * 1000} milliseconds")
