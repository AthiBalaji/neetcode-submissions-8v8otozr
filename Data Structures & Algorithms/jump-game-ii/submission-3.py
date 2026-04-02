class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        res = 0 
        c =0
        while True:
            r = nums[c]
            temp = 0
            land = 0
            for i in range(1, r+1):
                if c+i < len(nums)-1:
                    if temp <= c+i+nums[c+i]:
                        temp = c+i + nums[c+i]
                        land = c+i
                else:
                    return res+1 
            res+=1
            c = land

        