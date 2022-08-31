import math
from time import time

class RMQ:
    MAX = 500
    def __init__(self) -> None:
        self.lookup = [[0] * RMQ.MAX for _ in range(RMQ.MAX)]

    def preprocess(self, arr, n):
        # constructing lookup table takes (n log n) times
        for i in range(n):
            self.lookup[i][0] = i

        j = 1
        while (1 << j) <= n:
            i = 0
            while i + (1 << j) - 1 < n:
                if arr[self.lookup[i][j-1]] < \
                    arr[self.lookup[i+(1 << (j - 1))][j-1]]:
                    self.lookup[i][j] = self.lookup[i][j-1]
                else:
                    self.lookup[i][j] = self.lookup[i+(1 << (j-1))][j-1]
                i += 1
            j += 1

    def query(self, arr, query):
        # query takes O(1)
        left = query[0]
        right = query[1]

        j = int(math.log2(right - left + 1))

        if arr[self.lookup[left][j]] <= arr[self.lookup[right-(1 << j)+1][j]]:
            print(f"Minimum in range [{left}, {right}] is {arr[self.lookup[left][j]]}")
            return
        print(f"Minimum in range [{left}, {right}] is {arr[self.lookup[right-(1 << j)][j]]}")


if __name__ == "__main__":
    arr = [7,2,3,0,5,10,3,12,18]
    n = len(arr)
    queries = [[0,4],[4,7],[7,8]]
    m = len(queries)

    start = time()
    rmq = RMQ()
    rmq.preprocess(arr, n)
    for query in queries:
        rmq.query(arr, query)
    print(f"Time elapsed : {(time() - start)} milliseconds")
        