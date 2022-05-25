# author : Sura Wankam

def count_parentheses(s):
    ans = 0
    balanced = 0
    for i in range(len(s)):
        balanced += 1 if s[i] == '(' else -1
        if balanced == -1:
            ans += 1
            balanced += 1
    return ans + balanced


if __name__ == "__main__":
    s = input()
    print(count_parentheses(s))



