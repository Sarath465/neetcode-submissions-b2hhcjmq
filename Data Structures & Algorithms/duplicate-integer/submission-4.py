class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  return max([count(i) for i in nums]) > 1
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False