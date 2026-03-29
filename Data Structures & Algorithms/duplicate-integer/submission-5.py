class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  return max([count(i) for i in nums]) > 1
        hashset = set()
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1:]:
                return True
        return False