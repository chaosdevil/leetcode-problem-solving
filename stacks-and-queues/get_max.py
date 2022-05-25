from time import time
import sys

ops = []
with open("stacks-and-queues/get_max_input.txt", "r") as file:
    n = int(file.readline().strip())

    opt = file.readline().strip()
    while opt:
        ops.append(opt)
        opt = file.readline().strip()


def getMax(operations, n):
    # Write your code here
    result = []
    maximum = -sys.maxsize
    stack = []
    for i in range(n):
        opt = operations[i].split(" ")
        if opt[0] == '1':
            val = int(opt[1])
            maximum = max(val, maximum)
            stack.append((val, maximum))
        elif opt[0] == '2':
            if stack:
                stack.pop()
            if not stack:
                maximum = -sys.maxsize
            else:
                maximum = stack[-1][1]
        else:
            if stack:
                result.append(str(stack[-1][1]))
    return result

start = time()
print("\n".join(getMax(ops, n)))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

