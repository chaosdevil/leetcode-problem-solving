from time import time

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        # base case
        current = "11"
        for _ in range(n-2):
            count = 0
            new_current = []
            i, j = 0, 0
            while i < len(current) and j < len(current):
                if current[i] == current[j]:
                    count += 1
                    j += 1
                elif current[i] != current[j]:
                    new_current.append(str(count) + current[i])
                    count = 0
                    i = j
                    j = i
            if count != 0:
                new_current.append(str(count) + current[j-1])
            current = "".join(new_current)
        return current


if __name__ == "__main__":

    n = 28

    solution = Solution()

    start = time()
    print(solution.countAndSay(n))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
