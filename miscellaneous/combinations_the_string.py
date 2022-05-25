s = input()

prev = -1
count = 0
groups = []
i = 0

while i <= len(s):
    if i == len(s):
        groups.append((count, prev))
        break
    elif prev != -1 and s[i] != prev:
        groups.append((count, prev))
        count = 0
    
    count += 1
    prev = s[i]
    i += 1
    
for group in groups:
    print(group, end=" ")

print()
