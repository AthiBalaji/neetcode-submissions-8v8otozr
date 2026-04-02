class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while(l<=r):
            m = (l+r)//2
            if(nums[m] == target):
                return m
            if(nums[r] == target):
                return r
            if(nums[l] == target):
                return l 
            if(nums[m]>nums[r]):
                if(nums[m]>target and target>nums[r]):
                    r= m-1
                elif((nums[m]>target and nums[r]>target) or nums[m]<target):
                    l=m+1
            else:
                if(nums[m]>target):
                    r=m-1
                elif(nums[m]<target and target>nums[r]):
                    r= m-1
                elif(nums[m]<target and target<nums[r]):
                    l= m+1
            
        return -1       

        