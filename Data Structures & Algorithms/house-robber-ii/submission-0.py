class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            a =nums[0]
            b = 0
            for i in range(1, len(nums)):
                temp =a 
                a = max(a, nums[i] + b)
                b=temp
            return max(a,b)
        
        if len(nums) ==1:
            return nums[0]
        else:
            return max(helper(nums[1:]), helper(nums[:-1]))
        