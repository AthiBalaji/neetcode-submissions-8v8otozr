class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """this step iterates over the array and 
         gives a set from the elements"""
        num_set = set(nums)
        
        longest_sequence_length = 0

        for num in nums:
            if num-1 not in num_set:
                x = num 
                temp =1
                while x+1 in num_set:
                    temp+=1
                    x+=1
                longest_sequence_length = max(temp, longest_sequence_length)
        return longest_sequence_length
                





        
        