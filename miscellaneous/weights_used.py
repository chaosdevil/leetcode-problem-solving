if __name__ == "__main__":
    n = int(input())

    x = 0
    weights = []
    total = 0
    while total < n:
        val = 3 ** x
        total += val
        weights.append(val)
        x += 1  

    left = weights[:]
    right = weights[:]
    left[x-1] = n

    left = left[::-1]
    right = right[::-1]

    a = left[0]
    b = 0
    for i in range(x):
        b += right[i]
        for j in range(1, x):
            a += left[i]
            if a > b:
                a -= left[i]
        if a == b:
            print(a, b)
            break
        # b -= right[i]