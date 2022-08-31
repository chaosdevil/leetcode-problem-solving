if __name__ == "__main__":
    matrix = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 5, 6, 11, 8],
        [0, 1, 7, 11, 9, 4],
        [0, 4, 6, 1, 3, 2],
        [0, 7, 5, 4, 2, 3],
    ]

    # build 2d prefix sum
    n = 5
    m = 6
    prefix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] \
                     - prefix[i-1][j-1] + matrix[i][j]

    print(prefix)
