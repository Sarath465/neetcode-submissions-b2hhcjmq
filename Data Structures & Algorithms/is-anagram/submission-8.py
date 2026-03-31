class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Assemble the freq hashmap
        freq = {}
        for s_char in s:
            if s_char in freq: 
                freq[s_char] = freq[s_char] + 1
            else:
                freq[s_char] = 1

        # 2. Given t subtract the frequencies and check for zero if valid anagram
        for t_char in t:
            if t_char not in freq:
                return False
            else:
                if freq[t_char] - 1 == 0:
                    del freq[t_char]
                else:
                    freq[t_char] = freq[t_char] - 1

        return len(freq) == 0