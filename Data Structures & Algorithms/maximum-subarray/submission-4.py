class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = None
        sum = 0
        n = len(nums)
        for r in range(n):
            sum+=nums[r]
            print("h", sum)
            if not res or sum > res:
                res = sum 
            if sum < 0:
                sum = 0
                print("q", sum)
        return res 
        
        