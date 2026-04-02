class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = [1]
        for i in range(1, len(nums)):
            pre = nums[i-1]*pre
            prefix.append(pre)
        suf = 1
        suffix = [1]
        for i in range(len(nums)-2, -1, -1):
            suf= nums[i+1]*suf
            suffix.append(suf)
        print(suffix)
        n = len(nums)
        result = []
        for i in range(n):
            print("i",i)
            result.append(prefix[i]*suffix[n-i-1])
        return result 


        