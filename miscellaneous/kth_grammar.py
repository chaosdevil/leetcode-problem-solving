from time import time

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 0:
            return 1 if self.kthGrammar(n-1, k // 2) == 0 else 0
        else:
            return 0 if self.kthGrammar(n-1, (k+1) // 2) == 0 else 1

    def IterativekthGrammar(self, n: int, k: int) -> int:
        ans = 1
        while n-1 != 0:
            if k % 2 == 0:
                ans = -ans
                k //= 2
            else:
                k = (k+1) // 2
            n -= 1
        return 0 if ans == 1 else 1


if __name__ == "__main__":
    n = 30
    k = 40059963394453223

    solution = Solution()
    start = time()
    print(solution.kthGrammar(n, k))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
    
    start = time()
    print(solution.IterativekthGrammar(n, k))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
