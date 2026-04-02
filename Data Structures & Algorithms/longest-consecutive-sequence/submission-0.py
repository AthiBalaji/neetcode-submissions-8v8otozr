class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        longest = 0 

        for num in nums:
            if((num -1) in numsset):
                continue
            else:
                temp =1
                tempnum =num
                while(tempnum+1 in numsset):
                    temp+=1
                    tempnum+=1
                if(temp>longest):
                    longest = temp
        return longest          
        