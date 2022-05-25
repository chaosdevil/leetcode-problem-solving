from time import time


class Solution:
    def myPow(self, x: float, n: int):
        if n == 0:
            return 1
        
        temp = self.myPow(x, int(n / 2))
        
        if n % 2 == 0:
            return temp * temp
        else:
            if n > 0:
                return x * temp * temp
            else:
                return (temp * temp) / x


if __name__ == "__main__":

    start = time()
    solution = Solution()
    print(solution.myPow(2.4031, 100))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

