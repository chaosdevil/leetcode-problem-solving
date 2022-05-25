from time import time

mean = 0.0
count = 0
maximum = 0.0

start = time()
with open('miscellaneous/Streaming_average_input.txt', 'r') as file:
    while True:
        try:
            num = float(file.readline().strip())
            mean = ((mean * (count)) + num) / (count + 1)
            if mean > maximum:
                maximum = mean
            count += 1
        except ValueError:
            print(round(maximum,2))
            break

print(f"Time elapsed : {(time() - start) * 1000} milliseconds")  
