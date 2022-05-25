from time import time


with open("stacks-and-queues/equal_stacks_input.txt", "r") as file:
    n1, n2, n3 = list(map(int, file.readline().rstrip().split()))

    h1 = list(map(int, file.readline().rstrip().split()))
    h2 = list(map(int, file.readline().rstrip().split()))
    h3 = list(map(int, file.readline().rstrip().split()))

def equalStacks(h1, h2, h3):
    # Write your code here
    total_a = sum(h1)
    total_b = sum(h2)
    total_c = sum(h3)

    i, j, k = 0, 0, 0

    while total_a != total_b or total_b != total_c:
        if total_a > total_b or total_a > total_c:
            while total_a > total_b or total_a > total_c:
                total_a -= h1[i]
                i += 1
        if total_b > total_a or total_b > total_c:
            while total_b > total_a or total_b > total_c:
                total_b -= h2[j]
                j += 1
        if total_c > total_a or total_c > total_b:
            while total_c > total_a or total_c > total_b:
                total_c -= h3[k]
                k += 1
    return total_a

start = time()
print(equalStacks(h1, h2, h3))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
