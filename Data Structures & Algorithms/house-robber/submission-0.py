class Solution:
    def rob(self, nums: List[int]) -> int:
        a =nums[0] 
        b =0
        for i in range(1, len(nums)):
            temp = a
            a = max(a, b +nums[i])
            b = temp
        return max(a,b)

        