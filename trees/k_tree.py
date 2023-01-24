from time import time

def solve(n, k, d, has_d, path=[], memo=dict()):
	if n == 0 and has_d:
	    return 1

	if n <= 0:
	    return 0
	    
	s = str(path)
	if s in memo:
	    return memo[s]
	
	count = 0
	
	for i in range(1, k+1):
	    path.append(i)
	    if i == d:
	        has_d = True
	    count += solve(n-i, k, d, has_d, path, memo)
	    memo[s] = count
	    path.pop()
	
	return count

if __name__ == "__main__":
	n, k, d = list(map(int, input().split(" ")))
	
	start = time()
	print(solve(n, k, d, False))
	print(f"Time elasped : {(time() - start) * 1000} milliseconds")