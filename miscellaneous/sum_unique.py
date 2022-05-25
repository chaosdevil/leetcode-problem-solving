def sum_unique(a, b, c):
    try:
        if b == a:
            b = 0
        if c == a or c == b:
            c = 0

        return a + b + c
    except:
        return "only numbers are accepted"


print(sum_unique(2,4,5))
print(sum_unique(2,2,5))
print(sum_unique(1,1,1))
print(sum_unique(5,5,2))
print(sum_unique(1,1,5))
print(sum_unique(1,2,2,2,3))
print(sum_unique(5,2,7,3,1,1,2,5))

print(sum_unique('3',1,1,2,3))
print(sum_unique(1,2,3,4,5))


