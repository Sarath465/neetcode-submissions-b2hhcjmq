class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s, d_t = {}, {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in d_s:
                    d_s[s[i]] = d_s[s[i]] + 1
                else:
                    d_s[s[i]] = 1
                if t[i] in d_t:
                    d_t[t[i]] = d_t[t[i]] + 1
                else:
                    d_t[t[i]] = 1
            return d_s == d_t
        return False