t = int(input())

while t > 0:
    n, k = list(map(int, input().split(" ")))
    s = list(map(int, input().split(" ")))
    prefix = [0] * (n+1)
    j = 0
    for i in range(n-k+1, n+1):
        prefix[i] = s[j]
        j += 1
    
    if k == 1:
        print("YES")
    else:
        a = [0] * (n+1)
        for i in range(n-k+2, n+1):
            a[i] = prefix[i] - prefix[i-1]
        
        flag = True
        for i in range(n-k+2, n+1):
            if a[i] > a[i+1]:
                flag = False
                break
        
        if not flag:
            print(prefix)
            print(a)
            print("NO")
        elif prefix[n-k+1] > a[n-k+2] * (n-k+1):
            print("NO")
        else:
            print("YES")
    
    t -= 1