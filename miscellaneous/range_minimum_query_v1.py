# this code is an example of range minimum query

from time import time


class RMQ:
    MAX = 500
    def __init__(self):
        self.lookup = [[0] * RMQ.MAX for _ in range(RMQ.MAX)]

    def preprocess(self, arr, n):
        # preprocessing is a process to construct lookup table
        # takes O(n^2) time complexity
        for i in range(n):
            self.lookup[i][i] = i
        
        for i in range(n):
            for j in range(i+1, n):
                if arr[self.lookup[i][j-1]] < arr[j]:
                    self.lookup[i][j] = self.lookup[i][j-1]
                else:
                    self.lookup[i][j] = j

    def query(self, arr, query):
        # query process takes O(1)
        left = query[0]
        right = query[1]
        result = arr[self.lookup[left][right]]
        print(f"Minimum in range [{left}, {right}] is {result}")


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