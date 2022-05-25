def cookies(k, A):
    # Write your code here
    cookies = []
    
    for i in range(1, len(A)):
        if A[i] < k:
            cookies.append((A[i-1]*1) + (A[i]*2))
    print(cookies)

A = [1, 2, 3, 9, 10, 12]
k = 7

cookies(k, A)