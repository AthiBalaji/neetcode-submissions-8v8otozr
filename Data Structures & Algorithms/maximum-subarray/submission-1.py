class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0] 
        sum = nums[0]
        n = len(nums)
        for r in range(1, n):
            sum+=nums[r]
            print("h", sum)
            if sum > res:
                res = sum 
            if sum < 0:
                if r <= n -1:
                    sum = 0
                print("q", sum)
        if n == 2:
            res = max(res, nums[1])
        return res 
        
        