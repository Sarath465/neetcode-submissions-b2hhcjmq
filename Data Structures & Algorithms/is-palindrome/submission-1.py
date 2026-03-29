class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res = "".join([res, i.lower()])
        print(res, res[::-1])
        return res == res[::-1]
