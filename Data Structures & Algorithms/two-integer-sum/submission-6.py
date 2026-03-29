class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     if (target-nums[i]) in nums[i+1:]:
        #         return [i, nums.index(target-nums[i],i+1)]
        d = {}
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                return [d.get(target-nums[i]),i]
            d[nums[i]] = i
            