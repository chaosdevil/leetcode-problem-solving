from time import time


class Solution:

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]

            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)

            # put result in cache for later reference.
            cache[N] = result
            return result

        return recur_fib(N)


class SolutionV2:
    def fib(self, n: int) -> int:
        if n == 2:
            return 1
        if n < 2:
            return n
        
        memo = [0 for _ in range(n)]
        memo[0] = 0
        memo[1] = 1
        self.memoize_fib(n-1, memo)
        
        # print(memo)
        
        return memo[n-1]
        
    def memoize_fib(self, n, memo):
        if n <= 2:
            result = n
        else:
            result = self.memoize_fib(n-1, memo) + self.memoize_fib(n-2, memo)
        
        memo[n] = result
        
        return result

start = time()
solution = SolutionV2()
print(solution.fib(30))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")