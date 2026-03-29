class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d_s = {}
            d_t = {}
            for i in s:
                if i in d_s.keys():
                    d_s[i] = d_s[i]+1  
                else:
                    d_s[i]=1
            for i in t:
                if i in d_t.keys():
                    d_t[i] = d_t[i]+1
                else:
                    d_t[i]=1

            if d_s == d_t:
                return True
        return False
            

        