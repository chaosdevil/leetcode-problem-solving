def find_num_to_balance(s: str):
    balanced = 0
    ans = 0
    for i in range(len(s)):
        balanced += 1 if s[i] == '(' else -1
        if balanced == -1:
            ans += 1
            balanced += 1
    return balanced + ans

s = input()
print(find_num_to_balance(s))

