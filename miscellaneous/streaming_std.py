from math import sqrt
from time import time

sum1 = 0
sum2 = 0
count = 0
mean1, mean2 = 0.0, 0.0

start = time()
with open('miscellaneous/streaming_std_input.txt', 'r') as file:
    while True:
        try:
            num = float(file.readline().strip())
            sum1 = (sum1 + (num ** 2))
            mean1 = sum1 / (count + 1)
            sum2 = (sum2 + num)
            mean2 = (sum2 / (count + 1)) ** 2
            std = sqrt(mean1 - mean2)
            print(round(std, 2))
            count += 1
        except ValueError:
            break
    
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")