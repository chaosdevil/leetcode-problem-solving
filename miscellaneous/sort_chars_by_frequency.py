from time import time

class Solution:

    def find_max(self, freqs):
        max = 0
        key = 0
        for freq in freqs:
            if max < freq[1]:
                max = freq[1]
                key = freq[0]
        return key, max

    def frequencySort(self, s):
        freqs = dict()

        for c in s:
            if ord(c) not in freqs:
                freqs[ord(c)] = 1
            else:
                freqs[ord(c)] += 1

        freqs = sorted(freqs.items(), key=lambda x: x[0])
        # freqs = sorted(freqs, key=lambda x: ord(x[0]), reverse=False)
        res = ''
        for _ in range(len(freqs)):
            key, max = self.find_max(freqs)
            res += chr(key) * max
            freqs.remove((key, max))
        
        return res
        

if __name__ == '__main__':
    
    with open(r'C:\Users\yoksu\Desktop\algorithms\miscellaneous\sort_chars_by_frequency.txt', 'r') as file:
        inp = file.readline()

    start = time()
    solution = Solution()
    print(solution.frequencySort(inp))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")