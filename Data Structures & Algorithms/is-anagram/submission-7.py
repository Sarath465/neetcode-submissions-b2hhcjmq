class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s, d_t = {}, {}
        if len(s) == len(t):
            for i in range(len(s)):
                d_s[s[i]] = d_s.get(s[i],0) + 1
                d_t[t[i]] = d_t.get(t[i],0) + 1
            return d_s == d_t
        return False