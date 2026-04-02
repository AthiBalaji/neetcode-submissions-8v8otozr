class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        sum =1 
        for r in range(n-2, -1, -1):
            if nums[r] - sum >= 0:
                sum = 1
            else:
                sum+=1
        
        return sum == 1
        
        