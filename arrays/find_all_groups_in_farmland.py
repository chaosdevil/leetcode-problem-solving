from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        
        def find_max_coord(row, col):
            while row + 1 < m and land[row+1][col] == 1:
                row += 1
            while col + 1 < n and land[row][col+1] == 1:
                col += 1
            return [row, col]
        
        def clear(i, j, r, c):
            for x in range(i, r+1):
                for y in range(j, c+1):
                    land[x][y] = 0
        
        result = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    start = [i, j]
                    end = find_max_coord(i, j)
                    clear(i, j, end[0], end[1])
                    result.append(start + end)
            print(land)
        return result


if __name__ == "__main__":
    land = [[1,1,0,0,0,1],[1,1,0,0,0,0]]
    solution = Solution()
    print(solution.findFarmland(land))