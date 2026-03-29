class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  return max([count(i) for i in nums]) > 1
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] = d[i] + 1
            else:
                d[i] = 1
        return False if len(d)==0 else (max(d.values()) > 1)