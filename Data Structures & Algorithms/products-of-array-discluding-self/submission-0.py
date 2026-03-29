class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i in range(len(nums)):
            if i==0:
                prefix.append(1)
                suffix.append(1)
            elif i==1:
                prefix.append(nums[0])
                suffix.append(nums[len(nums)-1])
            else:
                prefix.append(prefix[i-1]*nums[i-1])
                suffix.append(suffix[i-1]*nums[len(nums)-i])
        print(prefix, suffix)
        return [prefix[i]*suffix[::-1][i] for i in range(len(prefix))]