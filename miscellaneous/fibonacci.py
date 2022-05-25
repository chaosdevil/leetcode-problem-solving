# code to print fibonacci series

def fibonacci(n):
    if n == 0:
        print(0)
        return
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(b, end=" ")
    print()

def print_fibonacci

def fibonacci_recursive(i, memo):
    if i == 0 or i == 1:
        return i
    if memo[i] == 0:
        memo[i] = fibonacci_recursive(i-1, memo) + fibonacci_recursive(i-2, memo)
    return memo[i]


fibonacci(13)