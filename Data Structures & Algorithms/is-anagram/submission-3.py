class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     d_s, d_t = {}, {}
        #     for i in range(len(s)):
        #         d_s[s[i]] = d_s.get(s[i],0) + 1
        #         d_t[t[i]] = d_t.get(t[i],0) + 1
        #     return d_s == d_t
        # return False
        # if len(s) == len(t):
        #     counts = [0]*26         
        #     for i in range(len(s)):
        #         counts[ord(s[i])-ord('a')] += 1
        #         counts[ord(t[i])-ord('a')] -= 1
        #     for val in counts:
        #         if val!=0:
        #             return False
        #     return True
        # return False
        s = list(s)
        t = list(t)
        if len(s) == len(t):
            for i in s:
                if i in t:
                    t.remove(i)
                else:
                    return False
            if len(t) == 0:
                return True
        return False