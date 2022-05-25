def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
        
    i = 0
    j = 0
        
    answer = 0
    s_set = set()
        
    while i < len(s):
        if i + j < len(s):
            if s[i+j] not in s_set:
                s_set.add(s[i+j])
                j += 1
            else:
                print(s_set)
                count = len(s_set)
                answer = max(count, answer)
                s_set = set()
                i += 1
                j = 0
        else:
            break
                
    return answer


if __name__ == "__main__":
    text = input()
    print(lengthOfLongestSubstring(text))


