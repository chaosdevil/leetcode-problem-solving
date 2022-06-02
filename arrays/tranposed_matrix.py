from time import time


class Solution:
    def transpose(self, matrix):
        n_rows, n_cols = len(matrix), len(matrix[0])

        # construct tranposed matrix
        t_mat = [[0 for _ in range(n_rows)] for _ in range(n_cols)]

        # fill values to transposed matrix
        for i in range(n_cols):
            for j in range(n_rows):
                t_mat[i][j] = matrix[j][i]

        return t_mat


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]

    start = time()
    solution = Solution()
    print(solution.transpose(matrix))
    print(f"Time elapsed : {(time() - start) * 1000}")