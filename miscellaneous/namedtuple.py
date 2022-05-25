from collections import namedtuple

n = int(input())
columns = [column for column in list(map(str, input().split(" "))) if column]
students = namedtuple('students', columns)

total = 0
for i in range(n):
    data = [data for data in map(str, input().split(" ")) if data]
    s = students(data[0], data[1], data[2], data[3])
    total += int(s.MARKS)

print(total / n)
    
    
