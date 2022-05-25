from ast import literal_eval
from typing import List

import heapq
from queue import PriorityQueue

class CustomQueue(PriorityQueue):
    def __init__(self, maxsize: int = ...) -> None:
        super().__init__(maxsize)
    
    def __lt__(self)


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [i for i in range(n)]

    def find(self, v):
        if v == self.root[v]:
            return v
        self.root[v] = self.find(self.root[v])
        return self.root[v]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return None

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_x] = root_y
            self.rank[root_y] += 1

class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # plan : dijkstra's algorithm
        
        m = len(heights)
        n = len(heights[0])
        
        distances = [[1e7 for _ in range(n)] for _ in range(m)]
        distances[0][0] = 0
        
        # add start point to queue
        # (distance, row, column)
        queue = PriorityQueue()
        queue.put((0, 0, 0))


        # create directions : up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            distance, row, col = queue.get()
            
            if distances[row][col] < distance:
                continue

            if row == m-1 and col == n-1:
                return distance
            
            # new_row, new_col = 0, 0
            for d in directions:
                dr = row + d[0]
                dc = col + d[1]
                if dr > -1 and dr < m:
                    if dc > -1 and dc < n:
                        new_diff = abs(heights[row][col] - heights[dr][dc])
                        new_diff = max(new_diff, distance)
                        if distances[dr][dc] > new_diff:
                            distances[dr][dc] = new_diff
                            queue.put((new_diff, dr, dc))

        return 0

    def minimumEffortPathV2(self, heights):
        m = len(heights)
        n = len(heights[0])

        pq = PriorityQueue()

        current_max = 1e6

        uf = UnionFind(m*n)

        for row in range(m):
            for col in range(n):
                if row != m-1:
                    pq.put([abs(heights[row][col]-heights[row+1][col]), row*n+col, (row+1)*n+col])
                elif col != n-1:
                    pq.put([abs(heights[row][col]-heights[row][col+1]), row*n+col, row*n+col+1])    

        while not uf.is_connected(0, m*n-1):
            arr = pq.get()
            if not uf.is_connected(arr[1], arr[2]):
                uf.union(arr[1], arr[2])
                current_max = min(arr[0], current_max)

        return current_max

with open(r"path_with_minimum_effort.txt", "r") as file:
    inp = literal_eval(file.readline())

# inp = [[1,2,2],[3,8,2],[5,3,5]]

solution = Solution()
print(solution.minimumEffortPathV2(inp))
                        
        

        