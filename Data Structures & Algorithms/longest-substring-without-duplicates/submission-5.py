class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        maxlen = 0
        l = 0
        for r in range(len(s)):
            print(f"s[r] is {s[r]} and charset is {charset}")
            while (s[r] in charset):
                charset.remove(s[l])
                l = l+1
            charset.add(s[r])
            maxlen = max(len(charset), maxlen)
            print(l,r,charset)
            
        return maxlen
        