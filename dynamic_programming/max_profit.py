from ast import literal_eval
from time import time

nums = literal_eval(input())


def max_profit(prices) -> int:

    max_profit = 0
    buy = prices[0]

    for i in range(1, len(prices)):
        current_profit = prices[i] - buy
        if current_profit < 0:
            buy = prices[i]
        if current_profit > max_profit:
            max_profit = current_profit
    
    return max_profit


if __name__ == "__main__":
    print(max_profit(nums))