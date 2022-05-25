import random
from time import time

class KnapSackProblem:
    def recursive_knapsack(self, capacity, n, weights, values):
        
        # recursive approach : O(2^n)
        if n == 0 or capacity == 0:
            return 0

        if weights[n-1] > capacity:
            return self.recursive_knapsack(capacity, n-1, weights, values)
        else:
            return max(values[n-1] + self.recursive_knapsack(capacity-weights[n-1], n-1, weights, values), 
                self.recursive_knapsack(capacity, n-1, weights, values))

    def my_knapsack(self, capacity, weights, values):

        n = len(weights)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            t_weight = capacity
            for j in range(i, n):
                t_weight -= weights[j]
                if t_weight >= 0:
                    dp[i][j] = max(dp[i][j-1] + values[j], dp[i][j-1])

        max_val = 0
        for i in range(len(dp)):
            if dp[i][n-1] > max_val:
                max_val = dp[i][n-1]
    
        return max_val

    def dp_knapsack(self, capacity, weights, values):
        dp = [0 for _ in range(capacity+1)] 
        
        for i in range(1, len(weights)+1):
            for w in range(capacity, -1, -1):
                if weights[i-1] <= w:
                    dp[w] = max(dp[w], dp[w-weights[i-1]] + values[i-1])

        return dp[capacity]

if __name__ == "__main__":
    
    random.seed(123)
    # capacity = 374000
    # values = [10, 15, 40, 42, 46, 50, 55, 70, 100, 200, 400]
    # weights = [1, 2, 3, 7, 11, 12, 20, 35, 70, 100, 150]
    # n = len(values)

    capacity = 3740000
    values = sorted([random.randint(1000,10000) for _ in range(10000)])
    weights = sorted([random.randint(1000,100000) for _ in range(10000)])
    n = len(values)

    knapsack = KnapSackProblem()

    # start = time()
    # print(knapsack.recursive_knapsack(capacity, n, weights, values))
    # print(f"Time elapsed : {(time() - start) * 1000} milliseconds\n")

    # start = time()
    # print(knapsack.dp_knapsack(capacity, weights, values))
    # print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    start = time()
    print(knapsack.my_knapsack(capacity, weights, values))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds\n")

