from time import time
from typing import List


class Solution:
    def numRefuel(self, d: int, m: int, s: List[int]) -> int:
        preserved_s = [0] * (d + 1)
        for i in s:
            preserved_s[i] = i

        count_refill = 0
        current = 0
        prev = 0
        while d > 0 and current < len(preserved_s):
            if current + m < len(preserved_s):
                if preserved_s[current+m] != 0:
                    current += m
                    d -= m
                    count_refill += 1
                    prev = current
                else:
                    # fall back
                    i = 0
                    while preserved_s[current+m-i] == 0:
                        i += 1
                    if preserved_s[current+m-i] == prev:
                        d -= m
                        count_refill += 1
                        break
                    # update m
                    if m == i:
                        current += m
                        d -= m
                        count_refill += 1
                        prev = current
                    else:
                        current += (m - i)
                        d -= (m - i)
                        count_refill += 1
                        prev = current
            else:
                d -= m
                count_refill += 1
        return count_refill - 1 if d <= 0 else -1


if __name__ == '__main__':
    solution = Solution()
    start = time()
    print(solution.numRefuel(15, 6, [1,2,4,5,6,8,10]))
    print(solution.numRefuel(20, 6, [2,5,6,9,12]))
    print(solution.numRefuel(20, 5, [2,5,6,9,12]))
    print(solution.numRefuel(20, 6, [2,5,6,9,14]))
    print(solution.numRefuel(28, 6, [4,5,7,9,14,16,22]))
    print(solution.numRefuel(28, 6, [4,5,7,9,14,16,25]))
    print(solution.numRefuel(28, 8, [4,5,7,9,14,16,24]))
    print(f"Time elasped : {(time() - start) * 1000} milliseconds")