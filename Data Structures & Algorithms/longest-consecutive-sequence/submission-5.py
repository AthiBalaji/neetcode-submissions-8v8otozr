class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if not nums:
            return 0
        longest = 1
        for elem in nums:
            if elem -1 in nums_set:
                continue
            temp = 1
            elem_copy = elem
            while elem_copy+1 in nums_set:
                elem_copy+=1
                temp+=1
                longest = max(longest, temp)
        return longest


            
        
        
        