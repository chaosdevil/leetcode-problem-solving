class KMP:
    def kmp_search(self, s, pattern):
        i = 0
        results = []
        p_len = len(pattern)

        while i < len(s) - p_len + 1:
            
            found = True

            sub_s = s[i:i+p_len]

            if sub_s != pattern:
                found = False
            
            if found:
                results.append(i)
            
            i += 1

        for k in range(len(results)):
            print(f"Found at index : {results[k]}")
            

if __name__ == "__main__":
    s = "ABABABCABABABCABABABC"
    pattern = "ABABAC"
    
    kmp = KMP()
    kmp.kmp_search(s, pattern)