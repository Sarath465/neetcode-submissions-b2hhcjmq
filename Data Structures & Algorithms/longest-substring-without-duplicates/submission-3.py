class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        if not s:
            return 0
        l, r = 0,1
        arr = [s[l]]
        maxs = len(arr)
        while r < len(s) and l < len(s):
            print(l, r, arr, maxs)
            if (s[r] in arr):
                l = l + 1
                r = l + 1
                arr = [s[l]]
                print(l, r, arr)
                # break
            else:
                arr.append(s[r])
                r = r+1
            maxs = max(len(arr), maxs)
        return maxs

                