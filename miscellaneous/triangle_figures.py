def print_triangle(n):
    print(f"Levels of triangle: {n}")

    for i in range(0, n):
        num = 0
        for _ in range(0, n-i-1):
            print(end="  ")
        for _ in range(0, i + 1):
            num += 1
            print(num, end='|')
        for _ in range(0, i):
            num -= 1
            print(num, end='|')
        print()

def print_triangle_v2(n):
    print(f"Levels of triangle: {n}")

    for j in range(n):
        for _ in range(n - (j+1)):
            print(end='  ')
        for i in range(j+1):
            print((i+1), end='|')
        for i in range(j):
            print((j-i), end='|')
        print()

print_triangle(9)
print_triangle_v2(9)
